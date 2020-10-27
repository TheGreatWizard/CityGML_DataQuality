import unittest
import os
from src.CityDB.Main import Main


class TestCityDBInteractions(unittest.TestCase):

    def test_create_connect_and_add_a_building(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        data_dir = os.path.join(dir_path, "data")
        m = Main()
        db_name = "test_extended"
        m.createDatabase(db_name)
        m.connect3dCityDB(db_name)
        m.importGML(os.path.join(data_dir, 'one_bld.gml'))
        sql = "select * from cityobject where gmlid='UUID_265e639d-fda7-11ea-a55a-00d861e16b8d';"
        rows = m.generalQuery(db_name, sql)
        self.assertTrue(isinstance(rows, list))
        self.assertTrue(len(rows) > 0)
        self.assertEquals(26, rows[0][1])
        self.assertEquals('UUID_265e639d-fda7-11ea-a55a-00d861e16b8d', rows[0][2])

    def test_main(self):
        m = Main()
        print(m)
