class CityObject:

    def __init__(self, **kwargs):
        self.cityobject_id = kwargs['cityobject_id'] if 'cityobject_id' in kwargs else ''
        self.instance_type = kwargs['instance_type'] if 'instance_type' in kwargs else 'all'
        self.ce90 = kwargs['ce90'] if 'ce90' in kwargs else None
        self.le90_2d = kwargs['le90_2d'] if 'le90_2d' in kwargs else None
        self.se90 = kwargs['se90'] if 'se90' in kwargs else None
        self.le90_3d = kwargs['le90_3d'] if 'le90_3d' in kwargs else None
        self.reliability = kwargs['reliability'] if 'reliability' in kwargs else None
        self.texturetype = kwargs['texturetype'] if 'texturetype' in kwargs else False
        self.resolution = kwargs['resolution'] if 'resolution' in kwargs else None
        self.measuredate = kwargs['measuredate'] if 'measuredate' in kwargs else None
        self.measuretime = kwargs['measuretime'] if 'measuretime' in kwargs else None
        self.transience = kwargs['transience'] if 'transience' in kwargs else None
        self.completeness = kwargs['completeness'] if 'completeness' in kwargs else None

    def insertSql(self):
        values = []
        sql = "INSERT INTO citydb.cityobject_dataquality("
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
