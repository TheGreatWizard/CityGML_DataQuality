import xml.etree.ElementTree as ET
from src.CityDB.Main import Main
from src.CityGML.Quality.Zone import Zone
from src.CityGML.Quality.CityObject import CityObject
from src.CityGML.Quality.Surface import Surface
from src.CityGML.Quality.SurfacePosition import SurfacePosition
from src.CityGML.Quality.Property import Property

import re


class QualityDataParser:

    def __init__(self, **kwargs):
        self.citygml_file = kwargs['citygml_file'] if 'citygml_file' in kwargs else None
        self.db_name = kwargs['db_name'] if 'db_name' in kwargs else None
        self.main = kwargs['main'] if 'main' in kwargs else None

        self.qualityData = {"zone": {}, "cityobject": {}, "property": {}}
        self.qualityObjects = None
        self.currentCityObject = None
        self.qualityNamespace = "http://www.opengis.net/citygml/quality/2.0"
        self.gmlNamespace = "http://www.opengis.net/gml"
        self.zoneId = 0
        self.instanceList = ['lod0FootPrint', 'lod0RoofEdge', 'lod1Solid', 'lod1MultiSurface',
                             'lod1TerrainIntersection',
                             'lod2Solid', 'lod2MultiSurface', 'lod2MultiCurve', 'lod2TerrainIntersection', 'lod3Solid',
                             'lod3MultiSurface', 'lod3MultiCurve', 'lod3TerrainIntersection', 'lod4Solid',
                             'lod4MultiSurface',
                             'lod4MultiCurve', 'lod4TerrainIntersection']

        self.name_map = {"completenessset": {'existence': 'existence',
                                             'completeness': 'completeness',
                                             'lod0': 'completeness_lod0',
                                             'lod1': 'completeness_lod1',
                                             'lod2': 'completeness_lod2',
                                             'lod3': 'completeness_lod3',
                                             'lod4': 'completeness_lod4',
                                             'mesh': 'mesh'},
                         "form1": {'target': 'target',
                                   'ce90': 'ce90',
                                   'le90': 'le90_2d'},
                         "form2": {'target': 'target',
                                   'se90': 'se90',
                                   'le90': 'le90_3d'},
                         "form3": {'targetsurface': 'target',
                                   'position': 'position',
                                   'azimuth_le90': 'azimuth_le90',
                                   'elevation_le90': 'elevation_le90',
                                   'texture_ce90': 'texture_ce90'},
                         "form4": {'targetlinestring': 'target',
                                   'positionaccuracy': 'positionaccuracy'}}

    def getCityObjectId(self, gmlid):
        sql = "select id from cityobject where gmlid='" + gmlid + "'"
        rows = self.main.generalQuery(self.db_name, sql)
        if len(rows) < 1:
            return None
        if len(rows[0]) < 1:
            return None
        return rows[0][0]

    def getSurfaceId(self, gmlid):
        sql = "select id from surface_geometry where gmlid='" + gmlid + "'"
        rows = self.main.generalQuery(self.db_name, sql)
        if len(rows) < 1:
            return None
        if len(rows[0]) < 1:
            return None
        return rows[0][0]

    def createObjects(self):
        qualityObjects = {"zone": [], "cityobject": [], "surface": [], "surfaceposition": [], "property": []}
        for key in self.qualityData['zone']:
            zone = Zone(**self.qualityData['zone'][key])
            qualityObjects["zone"].append(zone)

        for key in self.qualityData['cityobject']:
            cityobject_id = self.getCityObjectId(key)
            cityobject = CityObject(**self.qualityData['cityobject'][key], cityobject_id=cityobject_id)
            qualityObjects["cityobject"].append(cityobject)
            for name in self.qualityData['cityobject'][key]:
                if name in ['cityobject_id', 'ce90', 'le90_2d', 'se90', 'le90_3d', 'reliability', 'texturetype',
                            'resolution',
                            'measuredate', 'measuretime', 'transience', 'completeness']:
                    pass
                elif name in self.instanceList:
                    cityobjectinstance = CityObject(**self.qualityData['cityobject'][key][name],
                                                    cityobject_id=cityobject_id,
                                                    instance_type=name)
                    qualityObjects["cityobject"].append(cityobjectinstance)
                else:
                    if 'position' in self.qualityData['cityobject'][key][name]:
                        surface_id = self.getSurfaceId(name)
                        surface = Surface(**self.qualityData['cityobject'][key][name], surface_geometry_id=surface_id)
                        qualityObjects["surface"].append(surface)
                    elif 'positionaccuracy' in self.qualityData['cityobject'][key][name]:
                        polygon_index = name.strip('_').split("_")[-1]
                        n = len(polygon_index) + 2
                        surface_id = self.getSurfaceId(name[:-n])
                        surfaceposition = SurfacePosition(**self.qualityData['cityobject'][key][name],
                                                          surface_geometry_id=surface_id, polygon_index=polygon_index)
                        qualityObjects["surfaceposition"].append(surfaceposition)

        for key in self.qualityData['property']:
            gmlid = key.split("@")[0]
            target_property = key.split("@")[-1]
            cityobject_id = self.getCityObjectId(gmlid)
            prop = Property(**self.qualityData['property'][key], target_id=cityobject_id,
                            target_property=target_property)
            qualityObjects["property"].append(prop)
        self.qualityObjects = qualityObjects

    def getByGmlId(self, gmlid, element=None):
        if element is None:
            element = self.currentCityObject
        gmlid_ = '{' + self.gmlNamespace + '}id'
        if gmlid_ in element.attrib:
            if element.attrib[gmlid_] == gmlid:
                return element
        for child in element:
            result = self.getByGmlId(gmlid, child)
            if result is not None:
                return result
        return None

    def getByTag(self, tag, element=None):
        if element is None:
            element = self.currentCityObject
        if self.deleteNamespace(element.tag) == tag.lower():
            return element
        for child in element:
            result = self.getByTag(tag, child)
            if result is not None:
                return result
        return None

    def getManyByTag(self, tag, element=None):
        if element is None:
            element = self.currentCityObject
        output = []
        if self.deleteNamespace(element.tag) == tag.lower():
            output.append(element)
        for child in element:
            result = self.getManyByTag(tag, child)
            output.extend(result)
        return output

    @staticmethod
    def deleteNamespace(tag):
        res = re.findall('{([^\}]+)}', tag)
        if len(res) < 1:
            return tag
        return tag.replace("{" + res[0] + "}", "").lower()

    def parseQualityObject(self, element, name, parentData=None):
        if name in ["zone"]:
            self.zoneId += 1
            for zonechild in element:
                if self.qualityNamespace in zonechild.tag:
                    parentData = {'id': self.zoneId, 'otype': "zone"}
                    name = self.deleteNamespace(zonechild.tag)
                    self.parseQualityObject(zonechild, name, parentData)
            return

        if parentData is None:
            raise Exception("No parent data")
        if "otype" not in parentData:
            raise Exception("No otype")
        if "id" not in parentData:
            raise Exception("No id in parent data")

        otype = parentData['otype']
        id = parentData['id']
        if id not in self.qualityData[otype]:
            self.qualityData[otype][id] = {}
        if name in ["reliability", "realistic_texture", "texture_resolution", "completeness", "propertyName", "module"]:
            self.qualityData[otype][id][self.deleteNamespace(element.tag)] = element.text
        elif name in ["temporalreliability", "visualquality"]:
            for subelement in element:
                self.qualityData[otype][id][self.deleteNamespace(subelement.tag)] = subelement.text
        elif name in ["propertyreliability"]:
            propertyName = element.find("{" + self.qualityNamespace + "}propertyName").text.strip()
            for subelement in element:
                self.parseQualityObject(subelement, self.deleteNamespace(subelement.tag),
                                        {'otype': 'property', 'id': id + "@" + propertyName})
        elif name in ["completenessset"]:
            for subelement in element:
                tag = self.deleteNamespace(subelement.tag)
                if tag not in self.name_map[name]:
                    continue
                tag = self.name_map[name][tag].lower()
                self.qualityData[otype][id][tag] = subelement.text
        elif name in ["form1", "form2", "form3"]:
            obj = {}
            for subelement in element:
                tag = self.deleteNamespace(subelement.tag)
                if tag not in self.name_map[name]:
                    continue
                tag = self.name_map[name][tag].lower()
                if name == "form3" and tag == "position":
                    obj[tag] = [float(x) for x in re.split('\t| |\n', subelement.text)]
                else:
                    obj[tag] = subelement.text
            if "target" not in obj:
                self.qualityData[otype][id].update(obj)
            else:
                target = obj['target']
                del obj['target']
                self.qualityData[otype][id][target] = obj

        elif name in ["positionalquality"]:
            for pqchild in element:
                if self.qualityNamespace in pqchild.tag:
                    name = self.deleteNamespace(pqchild.tag)
                    self.parseQualityObject(pqchild, name, parentData)
        elif name in ["boundary"]:
            polygon = ET.Element("gml:Polygon")
            for elm in element:
                polygon.append(elm)
            element = ET.tostring(polygon, encoding='unicode', method='xml')
            self.qualityData[otype][id]['zone'] = element
            # z.setBoundary(boundary_str)
        elif name in ["form4"]:
            positionaccuracy = ''
            target = None
            for subelement in element:
                tag = self.deleteNamespace(subelement.tag)
                if tag not in self.name_map[name]:
                    continue
                tag = self.name_map[name][tag].lower()
                if tag == "target":
                    target = subelement.text
                elif tag == "positionaccuracy":
                    data = subelement.find('{' + self.gmlNamespace + '}posList').text
                    data_list = re.split('\t| |\n', data)
                    positionaccuracy = []
                    matset = []
                    while len(data_list) > 0:
                        val = data_list.pop(0)
                        if val == '':
                            continue
                        matset.append(float(val))
                        if len(matset) == 6:
                            positionaccuracy.append(matset)
                            matset = []

            if target is not None:
                self.qualityData[otype][id][target] = {'positionaccuracy': positionaccuracy}

    def parseCityElement(self, child, otype=None):
        parentData = {}
        gmlid = '{' + self.gmlNamespace + '}id'
        parentData['id'] = child.attrib[gmlid] if gmlid in child.attrib else None
        parentData['otype'] = otype
        for grandchild in child:
            if self.qualityNamespace in grandchild.tag:
                name = self.deleteNamespace(grandchild.tag)
                self.parseQualityObject(grandchild, name, parentData)
            else:
                self.parseCityElement(grandchild, "cityobject")

    def parseCityObject(self, cityObject):
        for child in cityObject:
            self.currentCityObject = cityObject
            if child.tag.endswith("zone"):
                self.parseQualityObject(child, "zone")
            else:
                self.parseCityElement(child, "cityobject")

    def parse(self):
        if self.citygml_file is None:
            raise Exception("No citygml file to parse")
        for key, ns in self.citygml_file.namespaces.items():
            ET.register_namespace(key, ns)
        for cityObject in self.citygml_file.objectIterator():
            self.parseCityObject(cityObject)
        self.createObjects()

    def importData(self):
        for key in self.qualityObjects:
            for obj in self.qualityObjects[key]:
                sql, values = obj.insertSql()
                self.main.generalInsert(self.db_name, sql, values)