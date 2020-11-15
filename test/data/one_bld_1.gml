<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<!-- Created with Liquid Studio 2020 (https://www.liquid-technologies.com) -->
<CityModel xmlns="http://www.opengis.net/citygml/2.0"
           xmlns:tran="http://www.opengis.net/citygml/transportation/2.0"
           xmlns:bldg="http://www.opengis.net/citygml/building/2.0"
           xmlns:gen="http://www.opengis.net/citygml/generics/2.0"
           xmlns:qlt="http://www.opengis.net/citygml/quality/2.0"
           xmlns:gml="http://www.opengis.net/gml"
           xmlns:xlink="http://www.w3.org/1999/xlink"
           xmlns:xAL="urn:oasis:names:tc:ciq:xsdschema:xAL:2.0"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="http://www.opengis.net/citygml/cityobjectgroup/2.0 http://schemas.opengis.net/citygml/cityobjectgroup/2.0/cityObjectGroup.xsd
           http://www.opengis.net/citygml/building/2.0 http://schemas.opengis.net/citygml/building/2.0/building.xsd 
           http://www.opengis.net/citygml/tunnel/2.0 http://schemas.opengis.net/citygml/tunnel/2.0/tunnel.xsd 
           http://www.opengis.net/citygml/waterbody/2.0 http://schemas.opengis.net/citygml/waterbody/2.0/waterBody.xsd 
           http://www.opengis.net/citygml/appearance/2.0 http://schemas.opengis.net/citygml/appearance/2.0/appearance.xsd 
           http://www.opengis.net/citygml/cityfurniture/2.0 http://schemas.opengis.net/citygml/cityfurniture/2.0/cityFurniture.xsd 
           http://www.opengis.net/citygml/generics/2.0 http://schemas.opengis.net/citygml/generics/2.0/generics.xsd 
           http://www.opengis.net/citygml/bridge/2.0 http://schemas.opengis.net/citygml/bridge/2.0/bridge.xsd 
           http://www.opengis.net/citygml/vegetation/2.0 http://schemas.opengis.net/citygml/vegetation/2.0/vegetation.xsd 
           http://www.opengis.net/citygml/transportation/2.0 http://schemas.opengis.net/citygml/transportation/2.0/transportation.xsd 
           http://www.opengis.net/citygml/relief/2.0 http://schemas.opengis.net/citygml/relief/2.0/relief.xsd 
           http://www.opengis.net/citygml/landuse/2.0 http://schemas.opengis.net/citygml/landuse/2.0/landUse.xsd
           http://www.opengis.net/citygml/quality/2.0 file:///C:/Users/banan/PycharmProjects/CityGML_DataQuality/bin/schemes/DataQuality.xsd
           http://www.opengis.net/citygml/2.0 http://schemas.opengis.net/citygml/2.0/cityGMLBase.xsd
           http://www.opengis.net/gml http://schemas.opengis.net/gml/3.1.1/base/gml.xsd">
    <gml:boundedBy>
        <gml:Envelope srsName="urn:ogc:def:crs:EPSG::25833" srsDimension="3">
            <gml:lowerCorner>389766.003191636 5817577.38103416 37.8899993896484</gml:lowerCorner>
            <gml:upperCorner>389782.046133584 5817596.1481637 49.0227358451254</gml:upperCorner>
        </gml:Envelope>
    </gml:boundedBy>
    <cityObjectMember>
        <qlt:zone>
            <qlt:boundary>
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
            </qlt:boundary>
            <qlt:module>Buildings</qlt:module>
            <qlt:completenessSet>
                <qlt:existence>true</qlt:existence>
                <qlt:completeness>0.9</qlt:completeness>
                <qlt:lod0>0</qlt:lod0>
                <qlt:lod1>0</qlt:lod1>
                <qlt:lod2>1</qlt:lod2>
                <qlt:lod3>0</qlt:lod3>
                <qlt:lod4>0</qlt:lod4>
                <qlt:mesh>0</qlt:mesh>
            </qlt:completenessSet>
            <qlt:temporalReliability>
                <qlt:measureDate>2020-11-02</qlt:measureDate>
                <qlt:measureTime>16:06</qlt:measureTime>
                <qlt:transience>112</qlt:transience>
            </qlt:temporalReliability>
            <qlt:positionalQuality>
                <qlt:form1>
                    <qlt:CE90>3.5</qlt:CE90>
                    <qlt:LE90>1.5</qlt:LE90>
                </qlt:form1>
                <qlt:form2>
                    <qlt:SE90>4.2</qlt:SE90>
                    <qlt:LE90>2.2</qlt:LE90>
                </qlt:form2>
            </qlt:positionalQuality>
            <qlt:realistic_texture>0</qlt:realistic_texture>
            <qlt:texture_resolution>0.15</qlt:texture_resolution>
        </qlt:zone>
    </cityObjectMember>
    <cityObjectMember>
        <bldg:Building gml:id="UUID_265e639d-fda7-11ea-a55a-00d861e16b8d">
            <qlt:reliability>0.99</qlt:reliability>
            <qlt:positionalQuality>
                 <qlt:form1>
                    <qlt:CE90>4.8</qlt:CE90>
                    <qlt:LE90>4.8</qlt:LE90>
                </qlt:form1>
                <qlt:form1>
                    <qlt:target>lod0FootPrint</qlt:target>
                    <qlt:CE90>1.5</qlt:CE90>
                    <qlt:LE90>1.5</qlt:LE90>
                </qlt:form1>
                <qlt:form2>
                    <qlt:target>lod2MultiSurface</qlt:target>
                    <qlt:SE90>1.5</qlt:SE90>
                    <qlt:LE90>1.5</qlt:LE90>
                </qlt:form2>
                <qlt:form3>
                    <qlt:targetSurface>GEOM_7300027</qlt:targetSurface>
                    <qlt:position>1.5 1.5 1.5 0.1 0.1 0.01</qlt:position>
                    <qlt:azimuth_LE90>1.1</qlt:azimuth_LE90>
                    <qlt:elevation_LE90>0.8</qlt:elevation_LE90>
                    <qlt:texture_CE90>0.2</qlt:texture_CE90>
                </qlt:form3>
                <qlt:form4>
                    <qlt:targetLineString>GEOM_7300027_0_</qlt:targetLineString>
                    <qlt:positionAccuracy>
                        <gml:posList srsDimension="6">
                            1.5 1.5 1.5 0.1 0.1 0.01
                            1.5 1.5 1.5 0.1 0.1 0.01
                            1.5 1.5 1.5 0.1 0.1 0.01
                            1.5 1.5 1.5 0.1 0.1 0.01
                            1.5 1.5 1.5 0.1 0.1 0.01
                        </gml:posList>
                    </qlt:positionAccuracy>
                </qlt:form4>
            </qlt:positionalQuality>
            <qlt:visualQuality>
                <qlt:textureType>false</qlt:textureType>
                <qlt:resolution>0.45</qlt:resolution>
            </qlt:visualQuality>
            <qlt:temporalReliability>
                <qlt:measureDate>2017-10-22</qlt:measureDate>
                <qlt:measureTime>10:33:00</qlt:measureTime>
                <qlt:transience>100</qlt:transience>
            </qlt:temporalReliability>
            <qlt:completeness>1</qlt:completeness>
            <bldg:boundedBy>
                <bldg:GroundSurface gml:id="UUID_9c9e3d81-60f3-45bb-b1f9-0509e1e3e409">
                    <creationDate>2014-07-09</creationDate>
                    <bldg:lod2MultiSurface>
                        <gml:MultiSurface gml:id="UUID_56ca1589-d692-4a99-b87e-0231d604afd7">
                            <gml:surfaceMember>
                                <gml:Polygon gml:id="GEOM_7300027">
                                    <gml:exterior>
                                        <gml:LinearRing gml:id="GEOM_7300027_0_">
                                            <gml:posList srsDimension="3">
                                                389766.079919154 5817581.71383611
                                                37.8899993896484 389776.190768319 5817595.96074015 37.8899993896484
                                                389781.969168672 5817591.81500954 37.8899993896484 389771.8583198
                                                5817577.56810558 37.8899993896484 389766.079919154 5817581.71383611
                                                37.8899993896484
                                            </gml:posList>
                                        </gml:LinearRing>
                                    </gml:exterior>
                                </gml:Polygon>
                            </gml:surfaceMember>
                        </gml:MultiSurface>
                    </bldg:lod2MultiSurface>
                </bldg:GroundSurface>
            </bldg:boundedBy>
            <bldg:boundedBy>
                <bldg:RoofSurface gml:id="UUID_af75e832-330c-46dc-bafc-e764d559c9ee">
                    <qlt:form2>
                        <qlt:target>lod2MultiSurface</qlt:target>
                        <qlt:SE90>1.0</qlt:SE90>
                        <qlt:LE90>1.5</qlt:LE90>
                    </qlt:form2>
                    <qlt:propertyReliability>
                        <qlt:propertyName>Material</qlt:propertyName>
                        <qlt:reliability>0.8</qlt:reliability>
                        <qlt:temporalReliability>
                            <qlt:measureDate>2017-10-22</qlt:measureDate>
                            <qlt:measureTime>10:33:00</qlt:measureTime>
                            <qlt:transience>10000</qlt:transience>
                        </qlt:temporalReliability>
                    </qlt:propertyReliability>
                    <gen:stringAttribute name="Material">
                        <gen:value>Clay</gen:value>
                    </gen:stringAttribute>
                    <bldg:lod2MultiSurface>
                        <gml:MultiSurface gml:id="UUID_230bca4f-c1e9-41f3-a66c-69bd877571ae">
                            <gml:surfaceMember>
                                <gml:Polygon gml:id="GEOM_7300037">
                                    <gml:exterior>
                                        <gml:LinearRing gml:id="GEOM_7300037_0_">
                                            <gml:posList srsDimension="3">
                                                389776.190984136 5817595.96105962
                                                48.0082155296589 389777.022237079 5817590.98840217 49.0227358451254
                                                389781.96938449 5817591.81532901 48.0082155296589 389776.190984136
                                                5817595.96105962 48.0082155296589
                                            </gml:posList>
                                        </gml:LinearRing>
                                    </gml:exterior>
                                </gml:Polygon>
                            </gml:surfaceMember>
                            <gml:surfaceMember>
                                <gml:Polygon gml:id="GEOM_7300036">
                                    <gml:exterior>
                                        <gml:LinearRing gml:id="GEOM_7300036_0_">
                                            <gml:posList srsDimension="3">
                                                389777.022237079 5817590.98840217
                                                49.0227358451254 389776.190984136 5817595.96105962 48.0082155296589
                                                389766.080134969 5817581.71415558 48.0082155296589 389771.027325788
                                                5817582.5411466 49.0227358451254 389777.022237079 5817590.98840217
                                                49.0227358451254
                                            </gml:posList>
                                        </gml:LinearRing>
                                    </gml:exterior>
                                </gml:Polygon>
                            </gml:surfaceMember>
                            <gml:surfaceMember>
                                <gml:Polygon gml:id="GEOM_7300035">
                                    <gml:exterior>
                                        <gml:LinearRing gml:id="GEOM_7300035_0_">
                                            <gml:posList srsDimension="3">
                                                389781.96938449 5817591.81532901
                                                48.0082155296589 389777.022237079 5817590.98840217 49.0227358451254
                                                389771.027325788 5817582.5411466 49.0227358451254 389771.858535616
                                                5817577.56842506 48.0082155296589 389781.96938449 5817591.81532901
                                                48.0082155296589
                                            </gml:posList>
                                        </gml:LinearRing>
                                    </gml:exterior>
                                </gml:Polygon>
                            </gml:surfaceMember>
                            <gml:surfaceMember>
                                <gml:Polygon gml:id="GEOM_7300034">
                                    <gml:exterior>
                                        <gml:LinearRing gml:id="GEOM_7300034_0_">
                                            <gml:posList srsDimension="3">
                                                389771.027325788 5817582.5411466
                                                49.0227358451254 389766.080134969 5817581.71415558 48.0082155296589
                                                389771.858535616 5817577.56842506 48.0082155296589 389771.027325788
                                                5817582.5411466 49.0227358451254
                                            </gml:posList>
                                        </gml:LinearRing>
                                    </gml:exterior>
                                </gml:Polygon>
                            </gml:surfaceMember>
                        </gml:MultiSurface>
                    </bldg:lod2MultiSurface>
                </bldg:RoofSurface>
            </bldg:boundedBy>
            <bldg:boundedBy>
                <bldg:WallSurface gml:id="UUID_1de3506a-1e01-480a-9268-0233897c96df">
                    <creationDate>2014-07-09</creationDate>
                    <bldg:lod2MultiSurface>
                        <gml:MultiSurface gml:id="UUID_cd466e6f-5a5d-4377-94de-d955e4f5fad5">
                            <gml:surfaceMember>
                                <gml:Polygon gml:id="GEOM_7300029">
                                    <gml:exterior>
                                        <gml:LinearRing gml:id="GEOM_7300029_0_">
                                            <gml:posList srsDimension="3">
                                                389781.969168672 5817591.81500954
                                                37.8899993896484 389781.96938449 5817591.81532901 48.0082155296589
                                                389771.858535616 5817577.56842506 48.0082155296589 389771.8583198
                                                5817577.56810558 37.8899993896484 389781.969168672 5817591.81500954
                                                37.8899993896484
                                            </gml:posList>
                                        </gml:LinearRing>
                                    </gml:exterior>
                                </gml:Polygon>
                            </gml:surfaceMember>
                            <gml:surfaceMember>
                                <gml:Polygon gml:id="GEOM_7300032">
                                    <gml:exterior>
                                        <gml:LinearRing gml:id="GEOM_7300032_0_">
                                            <gml:posList srsDimension="3">
                                                389771.8583198 5817577.56810558
                                                37.8899993896484 389771.858535616 5817577.56842506 48.0082155296589
                                                389766.080134969 5817581.71415558 48.0082155296589 389766.079919154
                                                5817581.71383611 37.8899993896484 389771.8583198 5817577.56810558
                                                37.8899993896484
                                            </gml:posList>
                                        </gml:LinearRing>
                                    </gml:exterior>
                                </gml:Polygon>
                            </gml:surfaceMember>
                            <gml:surfaceMember>
                                <gml:Polygon gml:id="GEOM_7300031">
                                    <gml:exterior>
                                        <gml:LinearRing gml:id="GEOM_7300031_0_">
                                            <gml:posList srsDimension="3">
                                                389766.079919154 5817581.71383611
                                                37.8899993896484 389766.080134969 5817581.71415558 48.0082155296589
                                                389776.190984136 5817595.96105962 48.0082155296589 389776.190768319
                                                5817595.96074015 37.8899993896484 389766.079919154 5817581.71383611
                                                37.8899993896484
                                            </gml:posList>
                                        </gml:LinearRing>
                                    </gml:exterior>
                                </gml:Polygon>
                            </gml:surfaceMember>
                            <gml:surfaceMember>
                                <gml:Polygon gml:id="GEOM_7300030">
                                    <gml:exterior>
                                        <gml:LinearRing gml:id="GEOM_7300030_0_">
                                            <gml:posList srsDimension="3">
                                                389776.190768319 5817595.96074015
                                                37.8899993896484 389776.190984136 5817595.96105962 48.0082155296589
                                                389781.96938449 5817591.81532901 48.0082155296589 389781.969168672
                                                5817591.81500954 37.8899993896484 389776.190768319 5817595.96074015
                                                37.8899993896484
                                            </gml:posList>
                                        </gml:LinearRing>
                                    </gml:exterior>
                                </gml:Polygon>
                            </gml:surfaceMember>
                        </gml:MultiSurface>
                    </bldg:lod2MultiSurface>
                </bldg:WallSurface>
            </bldg:boundedBy>
        </bldg:Building>
    </cityObjectMember>
</CityModel>