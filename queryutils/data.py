
from itertools import chain
from os import path

QUERIES_CSV = "/Users/salspaugh/splunk-internship/data/storm_may2013/SearchAuditLogsApril1ToApril7.csv"

class Extensions:
    
    CSV = "csv"
    JSON = "json"

def get_users(limit=None, filename="", directory="", ext=""):
    if filename:
        ext = get_extension(filename)
        if ext == Extensions.CSV:
            from csvdata import get_users_from_file
        elif ext == Extensions.JSON:
            from jsondata import get_users_from_file
        return get_users_from_file(filename)
    if directory:
        if ext == Extensions.CSV:
            from csvdata import get_users_from_directory
        elif ext == Extensions.JSON:
            from jsondata import get_users_from_directory
        if limit:
            return get_users_from_directory(directory, limit=limit)
        return get_users_from_directory(directory)
    from csvdata import get_users_from_file
    return get_users_from_file(QUERIES_CSV)

def get_extension(file):
    return path.splitext(file)[1]

def flatten(list_of_lists):
    return chain.from_iterable(list_of_lists)

def get_queries(limit=None):
    user_generator = get_users() if limit is None else get_users(limit=limit)
    for users in user_generator:
        queries = [user.queries for user in users]
        yield flatten(queries)
