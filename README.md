# CityGML_DataQuality

CityGML data quality extensions. Contains ADE and code to work with 3DCityDB with data quality extension.


## Related projects

* CityGML https://www.ogc.org/standards/citygml

* 3DCityDB https://www.3dcitydb.org/3dcitydb/

* CityGML-tools https://github.com/citygml4j/citygml-tools

## How to use

1. Install Postgress 12 + pgAdmin
2. Install PostGIS
2. Install 3DCityDB
3. (Optional) Download citygml-tools project
4. Download this project 
5. update the configuration file `bin/configuration/conf.json`

### Use from command line

`cd <path to the project directory>\bin\PythonScript`


##### Create CityGML database with data-quality

`python createDatabase.py <database name>`


##### Drop CityGML database 

`python dropDatabase.py <database name>`

##### Import CityGML file to database

`python importCityGml.py <database name> <full path to citygml file>`