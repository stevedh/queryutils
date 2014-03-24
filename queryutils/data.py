
from itertools import chain
from os import path

class Version:

    UNDIAG_2012 = "undiag_2012"
    STORM_2013 = "storm_2013"
    UNDIAG_2014 = "undiag_2014"

def get_users(limit=None, filename="", directory="", version=Version.UNDIAG_2014):
    # TODO: Accept a list of filenames instead.
    from csvdata import get_users_from_file, get_users_from_directory
    if filename:
        if version == Version.UNDIAG_2012:
            from jsondata import get_users_from_file
        return get_users_from_file(filename)
    if directory:
        if version == Version.UNDIAG_2012:
            from jsondata import get_users_from_directory
        if limit:
            return get_users_from_directory(directory, limit=limit)
        return get_users_from_directory(directory)
    print "You must provide a data file or directory argument." # TODO: Raise error.

def get_extension(file):
    return path.splitext(file)[1]

def flatten(list_of_lists):
    return chain.from_iterable(list_of_lists)

def get_queries(limit=None):
    user_generator = get_users() if limit is None else get_users(limit=limit)
    for users in user_generator:
        queries = [user.queries for user in users]
        yield flatten(queries)
