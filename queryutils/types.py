
import inspect

class Type(object):

    ranks = {
        "Miscellaneous" :                       -2,
        "Macro" :                               -1,
        "Meta" :                                0,
        "InputtingSelection" :                  1,
        "FilterSelection" :                     2,  
        "Reorder" :                             3,
        "Rename" :                              4,
        "Projection" :                          5,
        "TransformingProjection" :              6,
        "ExtendedProjection" :                  7,
        "WindowingProjection" :                 8,
        "Join" :                                9,
        "Aggregation" :                         10, 
        "ComplexAggregation" :                  11, 
        "Transpose" :                           12
    }

    def __init__(self, type, name):
        self.typestr = type
        self.type = self._init_type(type)
        self.rank = Type.ranks[type]
        self.name = name

    def _init_type(self, type):
        members = dict(inspect.getmembers(self))
        return members[type]()

    def __lt__(self, other):
        if self.rank == other.rank:
            return self.type.varstring() < other.type.varstring()
        return self.rank < other.rank

    def __eq__(self, other):
        return self.rank == other.rank and self.type.varstring() == other.type.varstring()

    def __repr__(self):
        return ':'.join([self.name, str(self.rank), self.type.varstring()])
    
    def __str__(self):
        return self.name

    def set_attributes(self, attrs):
        for attr in attrs:
            vars(self.type)[attr] = True

    class InputtingSelection(object):
        """
        * different rows and columns that are function of external data, optionally formatted as a table
        crawl
        - inputlookup
        - inputcsv
        - loadjob
        - rest

        * different rows and columns that are a function of a saved search and the current data
        - savedsearch

        * different rows and columns that are function of metadata, optionally formatted as a table
        - audit
        dbinspect
        - history
        - metadata
        metasearch
        - typeahead
        
        * adds rows based on content of other rows
        - mvexpand
        """
        def __init__(self):
            self.inputs_metadata = False            # audit, history, metadata
            self.inputs_external_data = False       # inputcsv, inputlookup, loadjob, rest
            self.inputs_from_current_data = False   # savedsearch, multikv

        def varstring(self):
            attrs = [self.inputs_metadata,  
                        self.inputs_external_data,
                        self.inputs_from_current_data]
            attrs = [str(int(attr)) for attr in attrs]
            return ''.join(attrs)

    class FilterSelection(object):
        """
        - filter rows based on user input: regex, search, where
        - filter rows based on other rows: dedup, uniq
        - filter rows based on index: head, tail
        - filter rows based on metadata: input

        NOTES: Any truth-valued expression is permitted in the selection condition.
        """

        def __init__(self):
            self.by_user_string_match = False       # search, regex
            self.by_boolean_statement = False       # search, where
            self.by_other_row_match = False         # dedup, uniq
            self.by_index = False                   # dedup, head, tail
            self.by_metadata = False                # input

            self.also_sorts = False                 # dedup
            self.also_deletes = False               # dedup

        def varstring(self):
            attrs = [self.by_user_string_match,  
                        self.by_boolean_statement, 
                        self.by_other_row_match, 
                        self.by_index,   
                        self.by_metadata,
                        self.also_sorts,          
                        self.also_deletes]
            attrs = [str(int(attr)) for attr in attrs]
            return ''.join(attrs)
    
    class Projection(object):
        """
        - filter columns based on user input: fields
        - filter columns based on user input and format as a table: table
        """

        def __init__(self):                         # fields
            self.also_formats = False               # table
        
        def varstring(self):
            attrs = [self.also_formats] 
            attrs = [str(int(attr)) for attr in attrs]
            return ''.join(attrs)

    class ExtendedProjection(object):
        """
        * additional columns in each row that is a global function of metadata 
         f( { r_1 : (c_1,...,c_k), ..., r_s : (c_1,..,c_k) } ) 
             = { r_1 : (c_1,...,c_k,g_1(),...,g_n()), ..., r_s : (c_1,..,c_k,g_1(),...g_n()) }
        + addinfo

        * additional column(s) in each row that is function of other column(s) in same row 
        + addtotals row=True
        + extract (kv)
        kvform
        outputtext - this is a confusing name since it doesn't do what outputcsv does
        rangemap
        reltime
        + rex
        + strcat
        - tags
        typer
        + xmlkv
        xpath
        
        * additional column in each row that is function of same or other column(s) in same row and user input
        + eval
        + spath

        * additional column in each row that is a function of possible other rows, any columns, and user input
        + appendcols
        """

        def __init__(self):

            self.function_with_user_input_params = False    # eval, appendcols
            
            self.numeric_function = False                   # addtotals row=True, eval, appendcols
            self.string_function = False                    # extract (kv), eval, rex, strcat, xmlkv, appendcols, spath

            self.function_of_metadata = False               # addinfo, tags, appendcols
            self.function_of_single_columns = False         # rex, xmlkv, appendcols, spath
            self.function_of_multiple_columns = False       # addtotals row=True, extract (kv), eval, strcat, tags, appendcols
            self.function_of_subsearch = False              # appendcols

            self.multiple_columns_added = False             # addinfo, extract (kv), rex, xmlkv, tags, appendcols
            self.data_dependent_num_columns_added = False   # extract (kv), xmlkv, tags, appendcols

        def varstring(self):
            attrs = [self.function_with_user_input_params, 
                        self.numeric_function,         
                        self.string_function,
                        self.function_of_metadata,     
                        self.function_of_single_columns,
                        self.function_of_multiple_columns,
                        self.multiple_columns_added,
                        self.data_dependent_num_columns_added]
            attrs = [str(int(attr)) for attr in attrs]
            return ''.join(attrs)


    class WindowingProjection(object): 
        """
        * additional column(s) in each row that is function of other column(s) in prior rows
         f( { r_1 : (c_1,...,c_k), ..., r_s : (c_1,..,c_k) } ) 
             = { r_1 : (c_1,...,c_k, c_k+1 = g(r_1:c_i)), ..., r_s : (c_1,..,c_k, c_k+1 = g(r_1:c_i,...r_s:c_i)) }
        accum
        autoregress
        concurrency
        - delta
        streamstats
        trendline
        
        * additional column in each row that is function of a subset of previous rows, optionally after an aggregation 
         f( { r_i : (c_1,...,c_k), ..., r_j : (c_1,..,c_k) } ) 
             = { r_i : (c_1,...,c_k, c_k+1 = g(r_i)), ..., r_j : (c_1,..,c_k, c_k+1 = g(r_i,...r_j-1)) }
        anomalies
        """
        def __init__(self):
            pass

        def varstring(self):
            return ""


    class TransformingProjection(object):
        """
        * transform entries based on function of same entry and optionally user input
        f( r_data, c_data ) = v 
        - convert (g(x) = int(x)
        - fieldformat
        - fillnull (g(x) = not null)
        nomv
        - makemv
        - multikv
        - replace (g(x) = y if x == k, otherwise x)
        scrub (g(x) = anonymized x)
        setfields (g(x) = c)
        xmlunescape (g(x) = unescaped x)

        * transform entries based on function of other entries in the same column in all rows
        - bin (alias for bucket)
        - bucket
        bucketdir
        outlier

        * transform entries based on function of other entries in the same column in prior rows
        filldown
        """

        def __init__(self):
            self.function_of_same_entry = False     # convert, 
            self.function_of_same_row = False       # convert, fieldformat, 
                                                    # fillnull, makemv, replace
            self.function_of_other_rows = False     # bucket, bin

            self.string_domain = False              # convert, fieldformat, makemv, replace
            self.string_range = False               # fieldformat, replace
            
            self.numeric_domain = False             # bucket, bin
            self.numeric_range = False              # convert
            
            self.range_domain = False               # bucket, bin
            
            self.null_domain = False                # fillnull
            self.user_defined_range = False         # fillnull

        def varstring(self):
            attrs = [self.function_of_same_row, 
                        self.function_of_other_rows, 
                        self.string_domain,
                        self.string_range,
                        self.numeric_domain, 
                        self.numeric_range,
                        self.range_domain,
                        self.null_domain,
                        self.user_defined_range]
            attrs = [str(int(attr)) for attr in attrs]
            return ''.join(attrs)
            
    class Reorder(object):
        """
        - reorder: reverse, sort
        """
        def __init__(self):
            pass

        def varstring(self):
            return ""

    class Join(object):
        """
        * additional columns in each row that is function of columns of two rows, pairwise
        - join 
        - lookup
        selfjoin
        """
        def __init__(self):
            pass

        def varstring(self):
            return ""

    class Aggregation(object):
        """
        * additional row with columns that is function of same column in all rows 
        - addcoltotals
        - addtotals col=true
        - chart
        - sichart
        - timechart
        - sitimechart
        - stats
        - sistats
        - streamstats
        """
        def __init__(self):
            self.visualization_component = False    # chart, sichart,
                                                    # timechart, sitimechart
            self.reorders = False                   # rare, sirare, top, sitop
            self.applies_fixed_function = False     # rare, sirare, top, sitop, 
                                                    # addtotals col=true

        def varstring(self):
            attrs = [self.visualization_component,
                        self.reorders,
                        self.applies_fixed_function] 
            attrs = [str(int(attr)) for attr in attrs]
            return ''.join(attrs)


    class ComplexAggregation(object):
        """
        * additional column in each row that is function of other column(s) in all rows and possibly user input
        erex
        eventstats
        predict
        x11

        * additional column in each row that is function of (_raw) column in all rows and user input of previous command
        - relevancy - depends on previous command

        * additional column(s) in each row that is function of all columns in all rows
        cluster
        kmeans (also reorders)
        """
        def __init__(self):
            pass

        def varstring(self):
            return ""


    class Rename(object):
        """
        - rename: rename
        """
        def __init__(self):
            pass

        def varstring(self):
            return ""
   
    class Macro(object):
        """
        - Splunk macros: MACRO tokens
        """
        def __init__(self):
            pass

        def varstring(self):
            return ""
   
    class Miscellaneous(object):
        """
        - unclear how to categorize: abstract, overlap
        """
        def __init__(self):
            pass

        def varstring(self):
            return ""

    class Transpose(object):
        """
        - transpose: transpose
        """
        def __init__(self):
            pass

        def varstring(self):
            return ""
    
    class Meta(object):
        """
        * metacommand outputs data
        - collect
        - outputcsv
        - outputlookup
        sendemail

        * metacommand controls where computation occurs
        - localop

        * metacommand runs jobs in parallel
        multisearch
        
        * metacommand calls external command
        run
        script

        * metacommand removes data
        - delete
        """

        def __init__(self):
            self.controls_computation = False       # localop
            self.calls_external_command = False     #
            self.outputs_data = False               # collect, outputlookup, outputcsv
            self.removes_data = False               # delete

        def varstring(self):
            attrs = [self.controls_computation,
                        self.calls_external_command,
                        self.outputs_data,
                        self.removes_data] 
            attrs = [str(int(attr)) for attr in attrs]
            return ''.join(attrs)

    class Union(object):
        """
        * additional rows with possibly same or possibly different columns that is any function of anything
        append
        appendpipe

        set union

        """
    
    class Difference(object):
        """
        set difference

        """
    
    class Intersection(object):
        """
        set intersection

        """

    class Product(object):
        """
        """

    class Mystery(object):
        """
        * additional column(s) in each row that are any function of anything
        appendcols
        """
