
import csv
import dateutil.parser
import json
import os
import splparser.parser

from .user import *
from .query import *

from itertools import chain
from splparser.exceptions import SPLSyntaxError, TerminatingSPLSyntaxError

BYTES_IN_MB = 1048576
QUERIES_CSV = "/Users/salspaugh/splunk-internship/data/storm_may2013/SearchAuditLogsApril1ToApril7.csv"

default_data_dir = '.'
home_dir = os.path.expanduser("~")
vars_conf = home_dir + '/.art/vars.conf'
try:
    varfile = open(vars_conf, 'r')
    vars = json.load(varfile)
    default_data_dir = vars['default_data_dir']
except:
    pass

def get_queries(limit=50*BYTES_IN_MB):
    for users in get_users(limit=limit):
        queries = [user.queries for user in users]
        yield flatten(queries)

def flatten(lol):
    return chain.from_iterable(lol)

def get_users(limit=None):
    first = True
    users = {}
    with open(QUERIES_CSV) as datafile:
        reader = csv.reader(datafile)
        for line in reader:
            if first: 
                first = False
                continue
            result = parse_query_line(line)
            username = result['user']
            timestamp = float(dateutil.parser.parse(result['_time']).strftime('%s.%f'))
            search = result['search'].strip()
            #print search
            #query_string = search.encode('ascii', 'ignore')
            query_string = search.decode('utf-8')
            user = User(username)
            type = result['searchtype']
            range = result['range']
            if range != "":
                range = float(range)
            query = Query(query_string, timestamp, user, type, range) 
            if not username in users:
                users[username] = user
            users[username].queries.append(query)
    return [users.values()]

def parse_query_line(parts):
    results = {}
    #parts = line.split(',')
    results['user'] = parts[6]
    results['search'] = parts[4]
    results['_time'] = parts[9]
    results['searchtype'] = parts[0]
    results['range'] = parts[1]
    return results
