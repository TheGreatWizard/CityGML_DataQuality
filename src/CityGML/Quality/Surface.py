class Surface:

    def __init__(self, **kwargs):
        self.surface_geometry_id = kwargs['surface_geometry_id'] if 'surface_geometry_id' in kwargs else ''
        self.position = kwargs['position'] if 'position' in kwargs else None
        self.azimuth_le90 = kwargs['azimuth_le90'] if 'azimuth_le90' in kwargs else None
        self.elevation_le90 = kwargs['elevation_le90'] if 'elevation_le90' in kwargs else None
        self.texture_ce90 = kwargs['texture_ce90'] if 'texture_ce90' in kwargs else None
        self.propriety = kwargs['propriety'] if 'propriety' in kwargs else None
        self.occlusion = kwargs['occlusion'] if 'occlusion' in kwargs else None
        self.distanceToCamera = kwargs['distanceToCamera'] if 'distanceToCamera' in kwargs else None
        self.verticality = kwargs['verticality'] if 'verticality' in kwargs else None
        self.resolution = kwargs['resolution'] if 'resolution' in kwargs else None

    def insertSql(self):
        values = []
        sql = "INSERT INTO citydb.surface_dataquality("
        sql_blanks = ""
        first = True
        for key in self.__dict__:
            attr = getattr(self, key)
            if not attr is None:
                if not first:
                    sql += ','
                    sql_blanks += ","
                sql += key
                sql_blanks += "%s"
                values.append(attr)
                first = False
        sql += ") values(" + sql_blanks + ");"
        return sql, values
