
import math
import csv
from sqlite3 import connect

from argparse import ArgumentParser
from queryutils import get_user_sessions
from contextlib import closing

SCHEMA = "spl_queries_schema.sql"

def main(database, schema, filename="", directory=""):
    init_db(database, schema) 
    load_db(database, filename=filename, directory=directory)


def init_db(database, schema):
    execute_db_script(database, schema)


def execute_db_script(database, script):
    with closing(connect(database)) as db:
        with open(script) as f:
            db.cursor().executescript(f.read())
        db.commit()


def load_db(database, filename="", directory=""):
    db = connect(database)
    load_main(db, filename=filename, directory=directory)
    db.close()


def load_main(database, filename="", directory=""):
    user_id = 1
    session_id = 1
    query_id = 1
    for users in get_user_sessions(filename=filename, directory=directory):
        for user in users:
            print "Loaded user"
            insert_user(database, user_id, user.name, user.case)
            for (local_sid, session) in user.sessions.iteritems():
                insert_session(database, session_id, user_id)
                for query in session.queries:
                    insert_query(database, query_id, query.text, query.time,
                                 False, user_id, 
                                 query.searchtype, query.earliest_event, query.latest_event, query.range, 
                                 query.is_realtime, query.splunk_search_id, query.runtime, query.splunk_savedsearch_name, 
                                 session_id=session_id)
                    query_id += 1
                session_id += 1
            for query in user.autorecurring_queries:
                insert_query(database, query_id, query.text, query.time, True, user_id, 
                query.searchtype, query.earliest_event, query.latest_event, query.range, 
                query.is_realtime, query.splunk_search_id, query.runtime, query.splunk_savedsearch_name)
                query_id += 1
            user_id += 1


def insert_user(db, id, username, company):
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (id, name, company) VALUES (?,?, ?)", [id, username, company])
    db.commit()


def insert_session(db, id, userid):
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO sessions (id, user_id) VALUES (?,?)", [id, userid])
    db.commit()


def insert_query(db, id, text, time, autogenerated, user_id, 
                searchtype, earliest_event, latest_event, range,
                is_realtime, splunk_search_id, runtime, splunk_savedsearch_name,
                session_id=None):
    cursor = db.cursor()
    if session_id is not None:
        cursor.execute("INSERT INTO queries \
                            (id, text, time, autogenerated, user_id, searchtype, earliest_event, latest_event, range, is_realtime, splunk_search_id, runtime, splunk_savedsearch_name, session_id) \
                            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                       [id, text, time, autogenerated, user_id, searchtype, earliest_event, latest_event, range, is_realtime, splunk_search_id, runtime, splunk_savedsearch_name, session_id])
    else:
        cursor.execute("INSERT INTO queries \
                            (id, text, time, autogenerated, user_id) \
                            VALUES (?,?,?,?,?)",
                       [id, text, time, autogenerated, user_id])
    db.commit()


if __name__ == "__main__":

    parser = ArgumentParser("Demonstrates how to extract sessions from SPL query logs using the queryutils module.")
    parser.add_argument("database", metavar="DATABASE",
                        help="The name of the sqlite3 database to create or load.")
    parser.add_argument("-f", "--filename", # TODO: Accept a list of filenames instead.
                        help="A query log containing SPL query data. Specify this OR directory.")
    parser.add_argument("-d", "--directory",
                        help="A directory containing SPL query logs. Specify this OR filename.")

    args = parser.parse_args()

    if args.filename:
        main(args.database, SCHEMA, filename=args.filename)
    elif args.directory:
        main(args.database, SCHEMA, directory=args.directory)
    else:
        parser.print_help()