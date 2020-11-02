import sys
import os

sys.path.insert(0, '../..')
from src.CityDB.Main import Main

if __name__ == "__main__":
    n = len(sys.argv)
    if n > 3:
        print('To many arguments')
    if n < 3:
        print('not enough arguments')

    m = Main()
    db_name = sys.argv[1]
    gml_file = sys.argv[2]
    if not os.path.exists(gml_file):
        print("citygml file not found:", gml_file)
        exit(1)
    m.connect3dCityDB(db_name)
    m.importGML(gml_file=gml_file)
    print("Done")
