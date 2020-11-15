class SurfacePosition:

    def __init__(self, **kwargs):
        self.surface_geometry_id = kwargs['surface_geometry_id'] if 'surface_geometry_id' in kwargs else ''
        self.polygon_index = kwargs['polygon_index'] if 'polygon_index' in kwargs else ''
        self.position_accuracy = kwargs['positionaccuracy'] if 'positionaccuracy' in kwargs else None

    def insertSql(self):
        values = []
        sql = "INSERT INTO citydb.surface_position_quality("
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
