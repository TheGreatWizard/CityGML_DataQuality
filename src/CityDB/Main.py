import subprocess
import psycopg2
import json
import os


class Main:
    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        project_dir = os.path.dirname(os.path.dirname(dir_path))
        self.create_db_script = os.path.join(project_dir, r"bin\ShellScripts\CREATE_EXTENDED_DB.bat")
        self.drop_db_script = os.path.join(project_dir, r"bin\ShellScripts\DROP_EXTENDED_DB.bat")
        conf_file = os.path.join(project_dir, r"bin\configuration\conf.json")
        with open(conf_file, 'r') as j:
            self.conf_data = json.load(j)

        connection_details_file = os.path.join(project_dir, r"bin\ShellScripts\CONNECTION_DETAILS.bat")
        with open(connection_details_file, 'w') as cf:
            cf.write("set PGBIN=" + self.conf_data['PGBIN'] + "\n")
            cf.write("set PGHOST=" + self.conf_data['PGHOST'] + "\n")
            cf.write("set PGUSER=" + self.conf_data['PGUSER'] + "\n")
            cf.write("set PGPASSWORD=" + self.conf_data['PGPASSWORD'] + "\n")
            cf.write("set CITYDBROOT=" + self.conf_data['citydb_root'] + "\n")

    def GMLtoJSON(self, name):
        process = subprocess.Popen([self.conf_data['citygml_tools'], 'to-cityjson', name],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   universal_newlines=True,
                                   bufsize=0)
        process.stdin.close()
        # Fetch output
        for line in process.stdout:
            print(line.strip())
        process.wait()

    def JSONtoGML(self, name):
        process = subprocess.Popen([self.conf_data['citygml_tools'], "from-cityjson", name],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   universal_newlines=True,
                                   bufsize=0)
        process.stdin.close()
        # Fetch output
        for line in process.stdout:
            print(line.strip())
        process.wait()

    def createDatabase(self, name):
        process = subprocess.Popen([self.create_db_script, name],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   universal_newlines=True,
                                   bufsize=0)
        process.stdin.close()
        # Fetch output
        for line in process.stdout:
            print(line.strip())
        for line in process.stderr:
            print(line.strip())
        # process.kill()
        process.wait()

    def dropDatabase(self, name):
        process = subprocess.Popen([self.drop_db_script, name],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   universal_newlines=True,
                                   bufsize=0)
        process.stdin.close()
        # Fetch output
        for line in process.stdout:
            print(line.strip())
        for line in process.stderr:
            print(line.strip())
        process.kill()
        process.wait()

    def connect3dCityDB(self, db_name):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        template = os.path.join(dir_path, r"bin\template.xml")
        self.project_file = os.path.join(dir_path, r"bin\pf.xml")

        with open(template, 'r') as f:
            with open(self.project_file, 'w') as fp:
                line = f.readline()
                while line:
                    new_line = line.replace('%%CITY_DB%%', db_name)
                    fp.writelines([new_line])
                    line = f.readline()

        process = subprocess.Popen(
            ["java", r'-jar', self.conf_data['citydb_script'], '-shell', "-config",
             self.project_file, '-testConnection'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            bufsize=0)
        process.stdin.close()
        # Fetch output
        for line in process.stdout:
            print(line.strip())
        for line in process.stderr:
            print(line.strip())
        process.kill()
        process.wait()

    def importGML(self, gml_file):
        process = subprocess.Popen(
            ["java", r'-jar', self.conf_data['citydb_script'], '-shell', "-config",
             self.project_file, "-import",
             gml_file],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            bufsize=0)
        process.stdin.close()
        # Fetch output
        for line in process.stdout:
            print(line.strip())
        for line in process.stderr:
            print(line.strip())
        process.kill()
        process.wait()

    def exportKML(self, export_file):

        process = subprocess.Popen(
            ["java", r'-jar', self.conf_data['citydb_script'], '-shell', "-config",
             self.project_file, "-kmlExport",
             export_file],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            bufsize=0)
        process.stdin.close()
        # Fetch output
        for line in process.stdout:
            print(line.strip())
        for line in process.stderr:
            print(line.strip())
        process.kill()
        process.wait()

    def generalQuery(self, db_name, sql):
        with psycopg2.connect(host=self.conf_data['PGHOST'],
                              database=db_name,
                              user=self.conf_data['PGUSER'],
                              password=self.conf_data['PGPASSWORD']) as conn:
            with conn.cursor() as cur:
                conn.autocommit = True
                cur.execute(sql)

                row = cur.fetchall()
                return row

    def exportPartsToGeoJson(self, db_name, geojson):

        sql = """drop materialized view if exists res cascade;
        create materialized view res as 
        select c.id, c.gmlid,g.gmlid as subpart_uuid, c.objectclass_id as type, g.geometry from cityobject as c, surface_geometry as g where g.cityobject_id=c.id and g.geometry is not null;

        select jsonb_build_object(
            'type',     'FeatureCollection',
            'features', jsonb_agg(features.feature)
        )
        from (
          select jsonb_build_object(
            'type',   'Feature',
        	  'objectclass', type,
        	  'uuid',   gmlid,
        	  'subpart_uuid',   subpart_uuid,
            'geometry',   ST_AsGeoJSON(ST_SetSRID(geometry,32636))::jsonb
          ) as feature
          from res) features;
          """

        # m.dropDatabase(db_name)

        with psycopg2.connect(host=self.conf_data['PGHOST'],
                              database=db_name,
                              user=self.conf_data['PGUSER'],
                              password=self.conf_data['PGPASSWORD']) as conn:
            with conn.cursor() as cur:
                conn.autocommit = True
                cur.execute(sql)

                row = cur.fetchone()
                while row is not None:
                    with open(geojson, 'w') as f:
                        json.dump(row[0], f)
                    # print(row)
                    break
