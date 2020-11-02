@echo off
:: Shell script to create an instance of the 3D City Database
:: on PostgreSQL/PostGIS

cd /d %~dp0
:: read database connection details
call CONNECTION_DETAILS.bat
set CITYDB=%1

:: add PGBIN to PATH
set PATH=%PGBIN%;%PATH%;%SYSTEMROOT%\System32

:: cd to path of the shell script
::cd /d %~dp0

psql -U postgres -c "DROP DATABASE %CITYDB%;"
psql -U postgres -c "CREATE DATABASE %CITYDB%;"
psql -U postgres -d %CITYDB% -c "CREATE EXTENSION IF NOT EXISTS postgis;"
psql -U postgres -d %CITYDB% -c "CREATE EXTENSION IF NOT EXISTS postgis_raster;"
psql -U postgres -d %CITYDB% -c "CREATE EXTENSION IF NOT EXISTS postgis_sfcgal;"
psql -U postgres -d %CITYDB% -c "CREATE EXTENSION IF NOT EXISTS postgis_topology;"

:: cd to path of the SQL scripts
cd %CITYDBROOT%/3dcitydb/postgresql/SQLScripts

:: Prompt for SRSNO -----------------------------------------------------------
:srid
set SRSNO=32636

:: Prompt for HEIGHT_EPSG -----------------------------------------------------
:height_epsg
set HEIGHT_EPSG=0

:: Prompt for GMLSRSNAME ------------------------------------------------------
:srsname
set var=
if %HEIGHT_EPSG% GTR 0 (
  set GMLSRSNAME=urn:ogc:def:crs,crs:EPSG::%SRSNO%,crs:EPSG::%HEIGHT_EPSG%
) else (
  set GMLSRSNAME=urn:ogc:def:crs:EPSG::%SRSNO%
)

:: Run CREATE_DB.sql to create the 3D City Database instance ------------------
echo.
echo Creating "%PGUSER%@%PGHOST%:%PGPORT%/%CITYDB%" ...
psql -d "%CITYDB%" -f "CREATE_DB.sql" -v srsno="%SRSNO%" -v gmlsrsname="%GMLSRSNAME%"

echo Adding data quality ADE tables ...

cd /d %~dp0
cd ..\SQLScripts\postgreSQL

psql -d "%CITYDB%" -f "CREATE_DATA_QUALITY_ADE_DB.sql" -v srsno="%SRSNO%"
exit