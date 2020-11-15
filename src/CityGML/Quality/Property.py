class Property:

    def __init__(self, **kwargs):
        self.target_id = kwargs['target_id'] if 'target_id' in kwargs else ''
        self.target_table = kwargs['target_table'] if 'target_table' in kwargs else None
        self.target_property = kwargs['target_property'] if 'target_property' in kwargs else None
        self.accuracy = kwargs['accuracy'] if 'accuracy' in kwargs else None
        self.accuracy = kwargs['accuracy'] if 'accuracy' in kwargs else None
        self.reliability = kwargs['reliability'] if 'reliability' in kwargs else None
        self.measuredate = kwargs['measuredate'] if 'measuredate' in kwargs else None
        self.measuretime = kwargs['measuretime'] if 'measuretime' in kwargs else None
        self.transience = kwargs['transience'] if 'transience' in kwargs else None

    def insertSql(self):
        values = []
        sql = "INSERT INTO citydb.property_dataquality("
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
