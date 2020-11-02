import sys
import os

sys.path.insert(0, '../..')
from src.CityDB.Main import Main

if __name__ == "__main__":
    n = len(sys.argv)
    if n > 2:
        print('To many arguments')
    if n < 2:
        print('Please give database name to create')

    m = Main()
    db_name = sys.argv[1]
    m.createDatabase(db_name)
    print("Done")
    print(db_name + " Database schema created with data quality extension.")
