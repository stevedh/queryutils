
import csv
import dateutil.parser
import os
import splparser.parser

from user import *
from query import *

from splparser.exceptions import SPLSyntaxError, TerminatingSPLSyntaxError

BYTES_IN_MB = 1048576

def get_users_from_file(filename):
    first = True
    users = {}
    with open(filename) as datafile:
        reader = csv.DictReader(datafile)
        for row in reader:
            username = row['user']
            timestamp = float(dateutil.parser.parse(row['_time']).strftime('%s.%f'))
            search = row['search'].strip()
            query_string = search.decode('utf-8')
            user = User(username)
            type = row['searchtype']
            range = row['range']
            if range != "":
                range = float(range)
            query = Query(query_string, timestamp, user, type, range) 
            if not username in users:
                users[username] = user
            users[username].queries.append(query)
    return [users.values()]

def get_users_from_directory(limit=50*BYTES_IN_MB):
    raw_data_files = get_csv_files(limit=limit)
    for f in raw_data_files:
        return get_users_from_file(f)

def get_csv_files(dir, limit=1000*BYTES_IN_MB):
    csv_files = []
    bytes_added = 0.
    for (dirpath, dirnames, filenames) in os.walk(dir):
        for filename in filenames:
            if filename[-5:] == '.csv': 
                full_filename = os.path.abspath(dir) + '/' + filename
                csv_files.append(full_filename) 
                bytes_added += os.path.getsize(full_filename)
                if bytes_added > limit:
                    return csv_files
    return csv_files
