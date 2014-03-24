#!/usr/bin/env python

from collections import defaultdict
from itertools import izip
from operator import itemgetter
from sets import *
import json
import re

from art.splqueryutils.data import *

def print_searches(splunk_results):
    for (key, value) in splunk_result_record_iter(splunk_results):
        if is_search(key):
            print value

def is_search(splunk_record_key):
    return splunk_record_key == 'search'

def tally_errors(jsonfiles):
    total_errors = 0.0
    for (key, value) in splunk_result_record_iter(jsonfiles):
        if is_error(key):
            total_errors += 1.0
    return total_errors

def print_pct_errors(total_errors, total_searches):
    print "total errors:", str(errors), str((total_errors / total_searches) * 100.0), "%"

def print_errored_searches(jsonfiles):
    for splunk_result in jsonfiles:
        for (key, value) in splunk_result.iteritems():
            if is_error(key):
                print splunk_result['search']

def tally_searches(jsonfiles):
    total_searches = 0.0
    for (key, value) in splunk_result_record_iter(jsonfiles):
        if is_search(key):
            total_searches += 1.0
    return total_searches

def tally_search_types(jsonfiles):
    total_searches = 0.0
    type_frequencies = defaultdict(float)
    for (key, value) in splunk_result_record_iter(jsonfiles):
        if is_search_type(key):
            type_frequencies[value] += 1.0
    return type_frequencies

def print_search_types(type_frequencies, total_searches):
    for (key, value) in type_frequencies.iteritems():
        print key, (value / total_searches) * 100.0, value
    print "all", 100.0, total_searches

def tally_duplicate_searches(jsonfiles):
    total_duplicates = 0.0
    duplicate_searches = defaultdict(float)
    for (key, value) in splunk_result_record_iter(jsonfiles):
        if is_search(key):
            duplicate_searches[value] += 1.0
    return duplicate_searches

def print_duplicates_per_unique_search(duplicate_searches):
    to_print_list = sorted(duplicate_searches.values())
    for value in to_print_list:
        print value

def print_example_duplicates(duplicate_searches, total_searches):
    print_threshhold = 1000.
    unprinted = 0.0
    to_print = defaultdict(float)
    for (key, value) in duplicate_searches.iteritems():
        if value < print_threshhold:
            to_print["Num dups below threshhold"] += float(value)
        else:
            to_print[key] = value
    #TODO: Try and make this function use less memory.
    to_print_list = sorted(to_print.iteritems(), key=lambda x: x[1], reverse=True)
    for (key, value) in to_print_list:
        print unicode(key)
        print "\t%2.3f\t%d" % ((value / total_searches)*100., value)
    print "ALL" 
    print "\t%d\t%d" % (100., total_searches)

def get_search_lengths_list(jsonfiles):
    return get_search_attr_list(jsonfiles, is_search_length)

def get_search_attr_list(jsonfiles, is_attr):
    search_attrs = []
    for (key, value) in splunk_result_record_iter(jsonfiles):
        if is_attr(key):
            search_attrs.append(float(value))
    search_attrs.sort()
    return search_attrs

def get_search_ranges_list(jsonfiles):
    return get_search_attr_list(jsonfiles, is_search_range)

def print_search_ranges(search_ranges):
    for search_range in search_lenghts:
        print search_range        

def print_search_lengths(search_lengths):
    for search_length in search_lenghts:
        print search_length        

def identity(anything):
    return anything

def get_search_attr_by_type(jsonfiles, is_attr, type_reclassifier=identity):
    search_attrs = defaultdict(list)
    for (key, value) in splunk_result_record_iter(jsonfiles):
        if is_search_type(key):
            search_type = type_reclassifier(value)
        elif is_attr(key):
            search_attr = float(value)
        search_attrs[search_type].append(search_attr)
    for search_attr_for_type in search_attrs.itervalues():
        search_attr_for_type.sort()
    return search_attrs

def get_search_length_by_type(jsonfiles, type_reclassifier=identity):
    return get_search_attr_by_type(jsonfiles, 
                is_search_length, type_reclassifier=type_reclassifier)

def get_search_range_by_type(jsonfiles, type_reclassifier=identity):
    return get_search_attr_by_type(jsonfiles, 
                is_search_range, type_reclassifier=type_reclassifier)

def print_search_lengths_by_type(search_lengths):
    for (search_type, search_lengths) in search_lengths.iteritems():
        max_search_length = max(len(search_lengths), max_search_length)
    first = True
    for key in search_lengths.keys():
        if not first:
            sys.stdout.write(',')
        first = False
        sys.stdout.write(key)
    for i in range(0, max_search_length):
        first = True
        for key in keylist:
            if not first:
                sys.stdout.write(',')
            else:
                sys.stdout.write('\n')
            first = False
            if i < len(search_lengths[key]):
                sys.stdout.write(str(search_lengths[key][i]))
            else:
                sys.stdout.write('-1') # ignore when plotting
    
def reclassify_search_type(search_type):
    if search_type == 'historical':
        return 'adhoc'
    elif search_type == 'remote':
        return 'SKIP'
    else:
        return 'scheduled'

def print_filtered_searches_by_commands(jsonfiles, cmds):
    for (key, value) in splunk_result_record_iter(jsonfiles):
        if is_search(key):
            search_stages = value.strip('|').split('|')
            cmds_in_search = [s.split()[0] for s in search_stages]
            discard = False
            for c in cmds_in_search:
                if not c in cmds:
                    discard = True
            if not discard:
                print unicode(value)

if __name__ == "__main__":

    import sys
    from optparse import OptionParser
    # TODO: Re-do handling of these options. 
    usage = "Usage: %prog [options] FILE [FILE FILE ...]"
    parser = OptionParser(usage=usage)
    parser.add_option("-e", "--errors",
        action="store_true", dest="errors", default=False,
        help="output the searches which resulted in error and their count")
    parser.add_option("-t", "--searchtypes",
        action="store_true", dest="searchtypes", default=False,
        help="output the search lengths of the searches in FILE(s)")
    parser.add_option("-l", "--searchlengths",
        action="store_true", dest="searchlengths", default=False,
        help="output the search lengths of the searches in FILE(s)")
    parser.add_option("-r", "--searchranges",
        action="store_true", dest="searchranges", default=False,
        help="output the search lengths of the searches in FILE(s)")
    parser.add_option("-d", "--duplicates",
        action="store_true", dest="duplicates", default=False,
        help="output the number of duplicates in the searches in FILE(s)")
    parser.add_option("-s", "--sessions",
        action="store_true", dest="sessions", default=False,
        help="output user sessions in the searches in FILE(s)")
    (options, args) = parser.parse_args()


    if len(args) < 1:
        parser.error("I need at least one FILE.")

    cmds = ['stats', 'eval', 'search', 'rename', 'table', 'head', 'tail', 'reverse', 'fields', 'top']
    print_filtered_searches_by_commands(args, cmds)
    exit(666)

    total_searches = tally_searches(args)

    if options.errors:
        total_errors = tally_errors(args) 
        print_pct_errors(total_errors, total_searches)
        errors(args)
        exit()
    if options.searchtypes:
        type_frequencies = tally_search_types(args)
        print_search_types(type_frequencies, total_searches)
        search_types(args)
        exit()
    if options.searchlengths:
        search_lengths = get_search_length_list(args)
        print_search_lengths(search_lengths) 
        exit()
    if options.searchranges:
        search_ranges = get_search_range_list(args)
        print_search_ranges(search_ranges) 
        exit()
    if options.duplicates:
        duplicate_searches = tally_duplicate_searches(args)
        #print_example_duplicates(duplicate_searches, total_searches)
        print_duplicates_per_unique_search(duplicate_searches)
        exit()
    if options.sessions:
        user_sessions = sessionize_searches(args)
        print_example_user_sessions(user_sessions)
        exit()
    
    parser.error("No option specified.")
