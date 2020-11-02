import sys
import os

sys.path.insert(0, '../..')
from src.CityDB.Main import Main

if __name__ == "__main__":
    n = len(sys.argv)
    if n > 2:
        print('To many arguments')
    if n < 2:
        print('Please give database name to drop')

    m = Main()
    db_name = sys.argv[1]
    m.dropDatabase(db_name)
    print("Done")
