
import sys

from .parse import *

class CommandsIndicatorFeatureVector(object):
    
    def __init__(self, n, query):
        self.sample_number = str(n)
        self.cmd_abstract = 0
        self.cmd_accum = 0
        self.cmd_addcoltotals = 0
        self.cmd_addinfo = 0
        self.cmd_addtotals = 0
        self.cmd_analyzefields = 0
        self.cmd_anomalies = 0
        self.cmd_anomalousvalue = 0
        self.cmd_append = 0
        self.cmd_appendcols = 0
        self.cmd_appendpipe = 0
        self.cmd_associate = 0
        self.cmd_audit = 0
        self.cmd_autoregress = 0
        self.cmd_bucket = 0
        self.cmd_bucketdir = 0
        self.cmd_chart = 0
        self.cmd_cluster = 0
        self.cmd_collect = 0
        self.cmd_concurrency = 0
        self.cmd_contingency = 0
        self.cmd_convert = 0
        self.cmd_correlate = 0
        self.cmd_crawl = 0
        self.cmd_dbinspect = 0
        self.cmd_dedup = 0
        self.cmd_delete = 0
        self.cmd_delta = 0
        self.cmd_diff = 0
        self.cmd_erex = 0
        self.cmd_eval = 0
        self.cmd_eventcount = 0
        self.cmd_eventstats = 0
        self.cmd_export = 0
        self.cmd_extract = 0
        self.cmd_kv = 0
        self.cmd_fieldformat = 0
        self.cmd_fields = 0
        self.cmd_fieldsummary = 0
        self.cmd_filldown = 0
        self.cmd_fillnull = 0
        self.cmd_findtypes = 0
        self.cmd_folderize = 0
        self.cmd_format = 0
        self.cmd_gauge = 0
        self.cmd_gentimes = 0
        self.cmd_head = 0
        self.cmd_highlight = 0
        self.cmd_history = 0
        self.cmd_iconify = 0
        self.cmd_input = 0
        self.cmd_inputcsv = 0
        self.cmd_inputlookup = 0
        self.cmd_iplocation = 0
        self.cmd_join = 0
        self.cmd_kmeans = 0
        self.cmd_kvform = 0
        self.cmd_loadjob = 0
        self.cmd_localize = 0
        self.cmd_localop = 0
        self.cmd_lookup = 0
        self.cmd_makecontinuous = 0
        self.cmd_makemv = 0
        self.cmd_map = 0
        self.cmd_metadata = 0
        self.cmd_metasearch = 0
        self.cmd_multikv = 0
        self.cmd_multisearch = 0
        self.cmd_mvcombine = 0
        self.cmd_mvexpand = 0
        self.cmd_nomv = 0
        self.cmd_outlier = 0
        self.cmd_outputcsv = 0
        self.cmd_outputlookup = 0
        self.cmd_outputtext = 0
        self.cmd_overlap = 0
        self.cmd_predict = 0
        self.cmd_rangemap = 0
        self.cmd_rare = 0
        self.cmd_regex = 0
        self.cmd_relevancy = 0
        self.cmd_reltime = 0
        self.cmd_rename = 0
        self.cmd_replace = 0
        self.cmd_rest = 0
        self.cmd_return = 0
        self.cmd_reverse = 0
        self.cmd_rex = 0
        self.cmd_rtorder = 0
        self.cmd_run = 0
        self.cmd_savedsearch = 0
        self.cmd_script = 0
        self.cmd_scrub = 0
        self.cmd_search = 0
        self.cmd_searchtxn = 0
        self.cmd_selfjoin = 0
        self.cmd_set = 0
        self.cmd_setfields = 0
        self.cmd_sendemail = 0
        self.cmd_sichart = 0
        self.cmd_sirare = 0
        self.cmd_sistats = 0
        self.cmd_sitimechart = 0
        self.cmd_sitop = 0
        self.cmd_sort = 0
        self.cmd_spath = 0
        self.cmd_stats = 0
        self.cmd_strcat = 0
        self.cmd_streamstats = 0
        self.cmd_table = 0
        self.cmd_tags = 0
        self.cmd_tail = 0
        self.cmd_timechart = 0
        self.cmd_top = 0
        self.cmd_transaction = 0
        self.cmd_transpose = 0
        self.cmd_trendline = 0
        self.cmd_typeahead = 0
        self.cmd_typelearner = 0
        self.cmd_typer = 0
        self.cmd_uniq = 0
        self.cmd_untable = 0
        self.cmd_where = 0
        self.cmd_x11 = 0
        self.cmd_xmlkv = 0
        self.cmd_xmlunescape = 0
        self.cmd_xpath = 0
        self.cmd_xyseries = 0
        self.nonfeature_attrs = ["cmd_sichart", "cmd_sirare", "cmd_sistats", "cmd_sitimechart", "cmd_sitop", "cmd_kv", "nonfeature_attrs", "extract_features", "sample_number"]
        self.extract_features(query)

    def __le__(self, other):
        if not isinstance(CommandIndicatorFeatureVector):
            raise TypeError("Can't compare CommandIndicatorFeatureVector with object of a different type.")
        selfvec = self.values_as_bitvector()
        othervec = other.values_as_bitvector()
        if sum(selfvec) < sum(othervec):
            return True
        if selfvec < othervec:
            return True
        return False

    def __eq__(self, other):
        if not isinstance(CommandIndicatorFeatureVector):
            raise TypeError("Can't compare CommandIndicatorFeatureVector with object of a different type.")
        selfvec = self.values_as_bitvector()
        othervec = other.values_as_bitvector()
        return (selvec == othervec)
    
    def extract_features(self, query):
        stages = break_into_stages(query)
        if len(filter(lambda x: len(x) == 0, stages)) > 0: 
            return # empty stage means it's an invalid query
        commands = [stage.split()[0] for stage in stages]
        for command in commands:
            setattr(self, "cmd_" + command, 1)
        self.collapse_identical_features()

    def collapse_identical_features(self):
        if self.cmd_sichart == 1: self.cmd_chart = 1
        if self.cmd_sirare == 1: self.cmd_rare = 1
        if self.cmd_sistats == 1: self.cmd_stats = 1
        if self.cmd_sitimechart == 1: self.cmd_timechart = 1
        if self.cmd_sitop == 1: self.cmd_top = 1
        if self.cmd_kv == 1: self.cmd_extract = 1
    
    def values_as_bit_vector(self):
        feature_attrs = filter(lambda x: x not in self.nonfeature_attrs, self.__dict__.keys())
        values = [str(getattr(self, attr)) for attr in sorted(feature_attrs)]
        return values

    def values_as_bit_string(self):
        feature_attrs = filter(lambda x: x not in self.nonfeature_attrs, self.__dict__.keys())
        values = [str(getattr(self, attr)) for attr in sorted(feature_attrs)]
        return ''.join(values)

    def print_csv_header(self):
        sys.stdout.write('"",') # for the data point ID
        for attr in sorted(self.__dict__.keys())[:-1]:
            if not attr in self.nonfeature_attrs:
                sys.stdout.write('"' + str(attr) + '",')
        sys.stdout.write('"' + sorted(self.__dict__.keys())[-1] + '"\n')
    
    def print_csv_values(self):
        sys.stdout.write('"' + self.sample_number + '",')
        for attr in sorted(self.__dict__.keys())[:-1]:
            if not attr in self.nonfeature_attrs:
                sys.stdout.write(str(getattr(self, attr)) + ',')
        sys.stdout.write(str(getattr(self, sorted(self.__dict__.keys())[-1])) + '\n')

    def readable_feature_tuples(self):
        tuples = []
        for attr in sorted(self.__dict__.keys()):
            if not attr in self.nonfeature_attrs:
                cmd = attr[4:]
                value = getattr(self, attr)
                tuples.append((cmd, value))
        return tuples
 
    def command_index_tuples(self):
        tuples = []
        index = 0
        for attr in sorted(self.__dict__.keys()):
            if not attr in self.nonfeature_attrs:
                cmd = attr[4:]
                tuples.append((cmd, index))
                index += 1
        return tuples
        
