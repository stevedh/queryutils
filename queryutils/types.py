
#class InputConstraints:
#
#    'AT_LEAST_ONE_NUMERICAL_COLUMN' = 0
#
#class OutputConstraints:
#
#    'ADDITIONAL_NUMERICAL_COLUMN' = 0
#    'ADDITIONAL_STRING_COLUMN' = 0
#
#        self.input_dimensions = 0
#        self.input_constraints = ''
#        self.output_dimensions = 0
#        self.output_constraints = ''
#        
#
#search_type = Type()
#search_type.input_dimensions = 0


class Type(object):
   
    class Selection(object):
    """
    * filter rows based on user input 
     f( { r_1 : (c_1,...,c_k), ..., r_s : (c_1,..,c_k) }, terms ) 
         = { r_1 : (c_1,...,c_k), ..., r_i-j : (c_1,...,c_k), r_i : (c_1,...,c_k), ..., r_s : (c_1,..,c_k) }
    delete
    regex
    search
    multisearch
    where

    * filter rows based on other rows
     f( { r_1 : (c_1,...,c_k), ..., r_s : (c_1,..,c_k) }, terms ) 
         = { r_1 : (c_1,...,c_k), ..., r_i-j : (c_1,...,c_k), r_i : (c_1,...,c_k), ..., r_s : (c_1,..,c_k) }
    dedup
    uniq

    * filter new rows based on other rows after generating new rows by any means
    set

    * filter rows based on index
    head
    tail

    * filter rows based on metadata
    input

    NOTES: Any truth-valued expression is permitted in the selection condition.
    """
    
    class Projection(object):
    """
    * filter columns based on user input, possibly formatted as a table
    fields
    table

    * additional column(s) in each row that is function of other column(s) in prior rows
     f( { r_1 : (c_1,...,c_k), ..., r_s : (c_1,..,c_k) } ) 
         = { r_1 : (c_1,...,c_k, c_k+1 = g(r_1:c_i)), ..., r_s : (c_1,..,c_k, c_k+1 = g(r_1:c_i,...r_s:c_i)) }
    accum
    autoregress
    concurrency
    delta
    streamstats
    trendline

    * additional column in each row that is function of other column(s) in all rows and possibly user input
    erex
    eventstats
    predict
    x11

    * additional column in each row that is function of other column in all rows, aggregated by other column, filtered by value of additional column
    rare
    sirare
    top
    sitop

    * additional column in each row that is function of (_raw) column in all rows and user input of previous command
    relevancy * depends on previous command

    * additional column(s) in each row that is function of all columns in all rows
    cluster
    kmeans (also reorders)

    * additional columns in each row that is a global function of metadata 
     f( { r_1 : (c_1,...,c_k), ..., r_s : (c_1,..,c_k) } ) 
         = { r_1 : (c_1,...,c_k,g_1(),...,g_n()), ..., r_s : (c_1,..,c_k,g_1(),...g_n()) }
    addinfo

    * additional column(s) in each row that is function of other column(s) in same row 
    addtotals
    extract (kv)
    kvform
    outputtext *this is a confusing name since it doesn't do what outputcsv does
    rangemap
    reltime
    rex
    strcat
    tag
    typer
    xmlkv
    xpath
    * additional column in each row that is function of same or other column(s) in same row and user input
    eval
    spath

    * additional column in each row that is function of a subset of previous rows, optionally after an aggregation 
     f( { r_i : (c_1,...,c_k), ..., r_j : (c_1,..,c_k) } ) 
         = { r_i : (c_1,...,c_k, c_k+1 = g(r_i)), ..., r_j : (c_1,..,c_k, c_k+1 = g(r_i,...r_j-1)) }
    anomalies

    * additional column(s) in each row that are any function of anything
    appendcols
    
    * transform entries based on function of same entry and optionally user input
    f( r_data, c_data ) = v 
    convert (g(x) = int(x)
    fieldformat
    fillnull (g(x) = not null)
    nomv
    makemv
    replace (g(x) = y if x == k, otherwise x)
    scrub (g(x) = anonymized x)
    setfields (g(x) = c)
    xmlunescape (g(x) = unescaped x)

    * transform entries based on function of other entries in the same column in all rows
    bucket
    bucketdir
    outlier

    * transform entries based on function of other entries in the same column in prior rows
    filldown

    NOTES: Includes extended projections.    
           Includes windowing.
    """

    class Join(object):
    """
    * additional columns in each row that is function of columns of two rows, pairwise
    join 
    selfjoin
    """
    
    class Aggregation(object):
    """
    * additional row with columns that is function of same column in all rows 
    f( { r_1 : (c_1,...,c_k), ..., r_s : (c_1,..,c_k) } ) 
        = { r_k+1 : (g(r_1:c_1,...,r_s:c_1),..., g(r_1:c_k,...,r_s:c_k) }
    addcoltotals
    addtotals col=true
    """

    class Rename(object):
    """
    * formatting
    rename
    """
    
    class Meta(object):
    """
    * metacommand outputs data
    collect
    outputcsv
    outputlookup
    sendemail

    * metacommand controls where computation occurs
    localop

    * metacommand calls external command
    run
    script
    """


    class Union(object):
    """
    * additional rows with possibly same or possibly different columns that is any function of anything
    append
    appendpipe
    """
    
    class Difference(object):
    """
    """
    
    class Product(object):
    """
    """

    def __init__(self):
        


