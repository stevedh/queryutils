
import csv
import dateutil.parser
import os
import splparser.parser

from user import *
from query import *

from os import path

from splparser.exceptions import SPLSyntaxError, TerminatingSPLSyntaxError

BYTES_IN_MB = 1048576
LIMIT = 2000*BYTES_IN_MB

def get_users_from_file(filename):
    first = True
    users = {}
    with open(filename) as datafile:
        reader = csv.DictReader(datafile)
        for row in reader:
            username = row.get('user', None)
            case = row.get('case_id', None)
            if case is not None:
                username = ".".join([username, case])
            user = User(username)
            user.case = case
            timestamp = float(dateutil.parser.parse(row.get('_time', None)).strftime('%s.%f'))
            search = row.get('search', None).strip()
            query_string = search.decode('utf-8')
            type = row.get('searchtype', None)
            if type is None:
                type = row.get('search_type', None)
            range = row.get('range', None)
            if range != "":
                range = float(range)
            query = Query(query_string, timestamp, user, type, range) 
            if not username in users:
                users[username] = user
            users[username].queries.append(query)
    return [users.values()]

def get_users_from_directory(directory, limit=LIMIT):
    raw_data_files = get_csv_files(directory, limit=limit)
    for f in raw_data_files:
        return get_users_from_file(f)

def get_csv_files(dir, limit=LIMIT):
    csv_files = []
    bytes_added = 0.
    for (dirpath, dirnames, filenames) in os.walk(dir):
        for filename in filenames:
            if filename[-4:] == '.csv': 
                full_filename = path.join(path.abspath(dir), filename)
                csv_files.append(full_filename) 
                bytes_added += path.getsize(full_filename)
                if bytes_added > limit:
                    return csv_files
    return csv_files
