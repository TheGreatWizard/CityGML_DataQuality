@echo off
:: Shell script to drop an instance of the 3D City Database
:: on PostgreSQL/PostGIS

cd /d %~dp0

:: read database connection details
call CONNECTION_DETAILS.bat
set CITYDB=%1

:: add PGBIN to PATH
set PATH=%PGBIN%;%PATH%;%SYSTEMROOT%\System32

echo.
echo Dropping "%PGUSER%@%PGHOST%:%PGPORT%/%CITYDB%" ...
psql -U postgres -c "DROP DATABASE %CITYDB%;"

exit