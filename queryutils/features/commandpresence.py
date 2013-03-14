
class CommandPresenceFeatureVector(object):
    
    def __init__(self, query):
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
        self.extract_features(query)

    def extract_features(self, query):
        stages = splqueryutils.parse.break_into_stages(query)
        commands = [stage.split()[0] for stage in stages]
        for command in commands:
            getattr(feature_vector, "cmd_" + command) = 1
        self.collapse_identical_features()

    def collapse_identical_features(self):
        if self.cmd_sichart = 1: self.cmd_chart = 1
        if self.cmd_sirare = 1: self.cmd_rare = 1
        if self.cmd_sistats = 1: self.cmd_stats = 1
        if self.cmd_sitimechart = 1: self.cmd_timechart = 1
        if self.cmd_sitop = 1: self.cmd_top = 1
        if self.cmd_kv = 1: self.cmd_extract = 1

    def output_as_csv(self):
        for attr in self.__dict__.keys()[:-1]:
            if not attr in self.redundant_attrs:
                print attr, ',',
        print self.__dict__.keys()[-1]
