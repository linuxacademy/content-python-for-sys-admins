import sys
import subprocess

def dump(url):
    try:
        return subprocess.Popen(['pg_dump', url], stdout=subprocess.PIPE)
    except OSError as err:
        print("Error: pg_dump not found")
        sys.exit(2)

def dump_file_name(url, timestamp=None):
    db_name = url.split("/")[-1]
    db_name = db_name.split("?")[0]
    if timestamp:
        return "%s-%s.sql" % (db_name, timestamp)
    else:
        return "%s.sql" % db_name
