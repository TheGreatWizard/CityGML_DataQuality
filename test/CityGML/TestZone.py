import unittest
import os
from src.CityGML.Quality.Zone import Zone


class TestZone(unittest.TestCase):

    def test_zone(self):
        geom = """ST_GeomFromGML('<gml:Polygon xmlns:gml=\"http://www.opengis.net/gml\">
                        <gml:exterior>
                            <gml:LinearRing>
                                <gml:posList srsDimension="2">
                                    389776.190984136 5817595.96105962
                                    389777.022237079 5817590.98840217
                                    389781.96938449 5817591.81532901 
                                    389776.190984136 5817595.96105962
                                </gml:posList>
                            </gml:LinearRing>
                        </gml:exterior>
                    </gml:Polygon>',32636)"""

        z = Zone(**{"parent_id": None, "zone": geom, "module": "Building", "existence": True, "completeness": 1,
                    "completeness_lod1": 1, "completeness_lod2": 1,
                    "completeness_lod3": 0.9, "completeness_lod4": 0, "mesh": None, "realistic_texture": None,
                    "texture_resolution": None, "ce90": None, "le90": None,
                    "measuredate": None, "measuretime": None})
        sql, values = z.insertSql()
        print(sql,values)

    def test_boundary(self):
        geom = """<qlt:boundary xmlns:gml="http://www.opengis.net/gml" xmlns:qlt="http://www.opengis.net/citygml/quality/2.0">
            <gml:exterior>
                <gml:LinearRing>
                    <gml:posList srsDimension="2">
                        389776.190984136 5817595.96105962
                        389777.022237079 5817590.98840217
                        389781.96938449 5817591.81532901 
                        389776.190984136 5817595.96105962
                    </gml:posList>
                </gml:LinearRing>
            </gml:exterior>
        </qlt:boundary>"""
        z = Zone()
        z.setBoundary(geom)
        print(z.zone)