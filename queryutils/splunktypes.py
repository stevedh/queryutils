from .types import *

implemented_commands = []

abstract_command = Type("Miscellaneous", "abstract")
implemented_commands.append(abstract_command)

addinfo_command = Type("ExtendedProjection", "addinfo")
addinfo_command.set_attributes(["function_of_metadata",
                                "multiple_columns_added"])
implemented_commands.append(addinfo_command)

addtotalsrow_command = Type("ExtendedProjection", "addtotals row")
addtotalsrow_command.set_attributes(["numeric_function",
                                     "function_of_multiple_columns"])
implemented_commands.append(addtotalsrow_command)

addtotalscol_command = Type("Aggregation", "addtotals col")
addtotalscol_command.set_attributes(["applies_fixed_function"])
implemented_commands.append(addtotalscol_command)

addcoltotals_command = Type("Aggregation", "addcoltotals")
addcoltotals_command.set_attributes(["applies_fixed_function"])
implemented_commands.append(addcoltotals_command)

anomalies_command = Type("WindowingProjection", "anomalies")
implemented_commands.append(anomalies_command)

append_command = Type("Union", "append")
implemented_commands.append(append_command)

appendcols_command = Type("ExtendedProjection", "appendcols")
appendcols_command.set_attributes(["function_with_user_input_params",
                                   "numeric_function",
                                   "string_function",
                                   "function_of_metadata",
                                   "function_of_single_columns",
                                   "function_of_multiple_columns",
                                   "function_of_subsearch",
                                   "multiple_columns_added",
                                   "data_dependent_num_columns_added"])
implemented_commands.append(appendcols_command)

appendpipe_command = Type("Union", "appendpipe")
implemented_commands.append(appendpipe_command)

audit_command = Type("InputMetadata", "audit")
implemented_commands.append(audit_command)

bin_command = Type("ExtendedProjection", "bin") # alias for bucket
implemented_commands.append(bin_command)

bucket_command = Type("ExtendedProjection", "bucket")
implemented_commands.append(bucket_command)

chart_command = Type("Aggregation", "chart")
chart_command.set_attributes(["visualization_component"])
implemented_commands.append(chart_command)

collect_command = Type("Cache", "collect")
implemented_commands.append(collect_command)

convert_command = Type("TransformingProjection", "convert")
convert_command.set_attributes(["function_of_same_entry",
                                    "string_domain",
                                    "numeric_range"])
implemented_commands.append(convert_command)

datamodel_command = Type("InputtingSelection", "datamodel")
implemented_commands.append(datamodel_command)

dbinspect_command = Type("InputMetadata", "dbinspect")
implemented_commands.append(dbinspect_command)

dedup_command = Type("FilterSelection", "dedup")
dedup_command.set_attributes(["by_other_row_match", 
                                "by_index",
                                "also_sorts",
                                "also_deletes"])
implemented_commands.append(dedup_command)

delete_command = Type("Meta", "delete")
delete_command.set_attributes(["removes_data"])
implemented_commands.append(delete_command)

delta_command = Type("WindowingProjection", "delta")
implemented_commands.append(delta_command)

eval_command = Type("ExtendedProjection", "eval")
eval_command.set_attributes(["function_with_user_input_params",
                                "numeric_function",
                                "string_function",
                                "function_of_multiple_columns"])
implemented_commands.append(eval_command)

eventstats_command = Type("ExtendedProjection", "eventstats") # aggregation and projection
implemented_commands.append(eventstats_command)

eventcount_command = Type("Aggregation", "eventcount")
implemented_commands.append(eventcount_command)

export_command = Type("Output", "export")
implemented_commands.append(export_command)

extract_command = Type("ExtendedProjection", "extract")
extract_command.set_attributes(["string_function",
                                    "function_of_multiple_columns",
                                    "multiple_columns_added",
                                    "data_dependent_num_columns_added"])
implemented_commands.append(extract_command)

fields_command = Type("Projection", "fields")
implemented_commands.append(fields_command)

fieldformat_command = Type("TransformingProjection", "fieldformat")
fieldformat_command.set_attributes(["function_of_same_entry",
                                        "string_domain",
                                        "string_range"])
implemented_commands.append(fieldformat_command)

filldown_command = Type("TransformingProjection", "filldown")
filldown_command.set_attributes(["function_of_other_rows",
                                 "function_of_same_column",
                                 "null_domain",
                                 "non_null_range"])
implemented_commands.append(filldown_command)

fillnull_command = Type("TransformingProjection", "fillnull")
fillnull_command.set_attributes(["function_of_same_entry", 
                                    "null_domain", 
                                    "user_defined_range"])
implemented_commands.append(fillnull_command)

gauge_command = Type("ExtendedProjection", "gauge")
implemented_commands.append(gauge_command)

head_command = Type("FilterSelection", "head")
head_command.set_attributes(["by_index"])
implemented_commands.append(head_command)

history_command = Type("InputMetadata", "history")
history_command.set_attributes(["inputs_metadata"])
implemented_commands.append(history_command)

inputlookup_command = Type("InputtingSelection", "inputlookup")
inputlookup_command.set_attributes(["inputs_external_data"])
implemented_commands.append(inputlookup_command)

inputcsv_command = Type("InputtingSelection", "inputcsv")
inputcsv_command.set_attributes(["inputs_external_data"])
implemented_commands.append(inputcsv_command)

iplocation_command = Type("ExtendedProjection", "iplocation")
implemented_commands.append(iplocation_command)

geostats_command = Type("Aggregation", "geostats")
implemented_commands.append(geostats_command)

join_command = Type("Join", "join")
implemented_commands.append(join_command)

kv_command = Type("ExtendedProjection", "kv")
kv_command.set_attributes(["string_function",
                                    "function_of_multiple_columns",
                                    "multiple_columns_added",
                                    "data_dependent_num_columns_added"])
implemented_commands.append(kv_command)

loadjob_command = Type("InputtingSelection", "loadjob")
loadjob_command.set_attributes(["inputs_external_data"])
implemented_commands.append(loadjob_command)

localop_command = Type("Meta", "localop")
localop_command.set_attributes(["controls_computation"])
implemented_commands.append(localop_command)

lookup_command = Type("Join", "lookup")
implemented_commands.append(lookup_command)

metadata_command = Type("InputtingSelection", "metadata")
metadata_command.set_attributes(["inputs_metadata"])
implemented_commands.append(metadata_command)

macro_command = Type("Macro", "macro")
implemented_commands.append(macro_command)

makemv_command = Type("TransformingProjection", "makemv")
makemv_command.set_attributes(["function_of_same_entry",
                                "string_domain"])
implemented_commands.append(makemv_command)

map_command = Type("Miscellaneous", "map")
implemented_commands.append(map_command)

metasearch_command = Type("Meta", "metasearch")
implemented_commands.append(metasearch_command)

multikv_command = Type("TransformingProjection", "multikv")
multikv_command.set_attributes(["string_domain",
                                "string_range"])
implemented_commands.append(multikv_command)

mvcombine_command = Type("Aggregation", "mvcombine")
implemented_commands.append(mvcombine_command)

mvexpand_command = Type("InputtingSelection", "mvexpand")
mvexpand_command.set_attributes(["inputs_from_current_data"])
implemented_commands.append(mvexpand_command)

nomv_command = Type("TransformingProjection", "nomv")
nomv_command.set_attributes(["string_domain",
                                "string_range"])
implemented_commands.append(nomv_command)

outlier_command = Type("TransformingProjection", "outlier")
outlier_command.set_attributes(["function_of_other_rows",
                                "function_of_same_entry",
                                "numeric_domain",
                                "numeric_range"])
implemented_commands.append(outlier_command)

outputcsv_command = Type("Output", "outputcsv")
implemented_commands.append(outputcsv_command)

outputlookup_command = Type("Output", "outputlookup")
implemented_commands.append(outputlookup_command)

outputtext_command = Type("ExtendedProjection", "outputtext")
implemented_commands.append(outputtext_command)

overlap_command = Type("Miscellaneous", "overlap")
implemented_commands.append(overlap_command)

rangemap_command = Type("ExtendedProjection", "rangemap")
implemented_commands.append(rangemap_command)

rare_command = Type("Aggregation", "rare")
rare_command.set_attributes(["reorders",
                                "applies_fixed_function"])
implemented_commands.append(rare_command)

regex_command = Type("FilterSelection", "regex")
regex_command.set_attributes(["by_user_string_match"])
implemented_commands.append(regex_command)

relevancy_command = Type("ExtendedProjection", "relevancy")
implemented_commands.append(relevancy_command)

rename_command = Type("Rename", "rename")
implemented_commands.append(rename_command)

replace_command = Type("TransformingProjection", "replace")
replace_command.set_attributes(["function_of_same_entry",
                                    "string_domain",
                                    "string_range"])
implemented_commands.append(replace_command)

rest_command = Type("InputtingSelection", "rest")
rest_command.set_attributes(["inputs_external_data"])
implemented_commands.append(rest_command)

return_command = Type("Miscellaneous", "return")
implemented_commands.append(return_command)

reverse_command = Type("Reorder", "reverse")
implemented_commands.append(reverse_command)

rex_command = Type("ExtendedProjection", "rex")
rex_command.set_attributes(["string_function",
                            "function_of_single_columns",
                            "multiple_columns_added"])
implemented_commands.append(rex_command)

savedsearch_command = Type("InputtingSelection", "savedsearch")
savedsearch_command.set_attributes(["inputs_from_current_data"])
implemented_commands.append(savedsearch_command)

search_command = Type("FilterSelection", "search")
search_command.set_attributes(["by_user_string_match",
                                "by_boolean_statement"])
implemented_commands.append(search_command)

sendemail_command = Type("Output", "sendemail")
implemented_commands.append(sendemail_command)

set_command = Type("Union", "set")
implemented_commands.append(set_command)

sichart_command = Type("Cache", "sichart")
implemented_commands.append(sichart_command)

sirare_command = Type("Cache", "sirare")
implemented_commands.append(sirare_command)

sistats_command = Type("Cache", "sistats")
implemented_commands.append(sistats_command)

sitimechart_command = Type("Cache", "sitimechart")
implemented_commands.append(sitimechart_command)

sitop_command = Type("Cache", "sitop")
implemented_commands.append(sitop_command)

sort_command = Type("Reorder", "sort")
implemented_commands.append(sort_command)

spath_command = Type("ExtendedProjection", "spath")
spath_command.set_attributes(["string_function",
                              "function_of_single_columns"])
implemented_commands.append(spath_command)

stats_command = Type("Aggregation", "stats")
implemented_commands.append(stats_command)

strcat_command = Type("ExtendedProjection", "strcat")
strcat_command.set_attributes(["string_function",
                                "function_of_multiple_columns"])
implemented_commands.append(strcat_command)

streamstats_command = Type("WindowingProjection", "streamstats")
implemented_commands.append(streamstats_command)

table_command = Type("Projection", "table")
table_command.set_attributes(["also_formats"])
implemented_commands.append(table_command)

tags_command = Type("ExtendedProjection", "tags")
tags_command.set_attributes(["function_of_metadata",
                            "function_of_multiple_columns",
                            "multiple_columns_added",
                            "data_dependent_num_columns_added"])
implemented_commands.append(tags_command)

tail_command = Type("FilterSelection", "tail")
tail_command.set_attributes(["by_index"])
implemented_commands.append(tail_command)

timechart_command = Type("Aggregation", "timechart")
timechart_command.set_attributes(["visualization_component"])
implemented_commands.append(timechart_command)

top_command = Type("Aggregation", "top")
top_command.set_attributes(["reorders",
                            "applies_fixed_function"])
implemented_commands.append(top_command)

transaction_command = Type("Aggregation", "transaction")
implemented_commands.append(transaction_command)

transpose_command = Type("Transpose", "transpose")
implemented_commands.append(transpose_command)

tscollect_command = Type("Cache", "tscollect")
implemented_commands.append(tscollect_command)

tstats_command = Type("Aggregation", "tstats")
implemented_commands.append(tstats_command)

typeahead_command = Type("InputMetadata", "typeahead")
implemented_commands.append(typeahead_command)

where_command = Type("FilterSelection", "where")
where_command.set_attributes(["by_boolean_statement"])
implemented_commands.append(where_command)

uniq_command = Type("FilterSelection", "uniq")
uniq_command.set_attributes(["by_other_row_match"])
implemented_commands.append(uniq_command)

xmlkv_command = Type("ExtendedProjection", "xmlkv")
xmlkv_command.set_attributes(["string_function",
                              "function_of_single_columns",
                              "multiple_columns_added",
                              "data_depended_columns_added"])
implemented_commands.append(xmlkv_command)

implemented_commands.sort()
 
names = [c.name for c in implemented_commands]
types = [c.typestr for c in implemented_commands]
command_type_lookup = dict(zip(names, types))

def lookup_category(stagenode):
    if type(stagenode) == type(""):
        return command_type_lookup.get(stagenode, None)
    command = stagenode.children[0].raw
    if command == "addtotals":
        command = detect_addtotals_type(stagenode)
    return command_type_lookup.get(command, None)

def detect_addtotals_type(stagenode):
    optionnodes = []
    for node in stagenode.itertree():
        if node.role == "EQ" and node.children[0].role == "OPTION":
            optionnodes.append(node)
    for optionnode in optionnodes:
        paramnode = optionnode.children[0]
        valuenode = optionnode.children[1]
        value = detect_truth_value(valuenode.raw)
        if value and paramnode.raw == "col":
            return "addtotals col"
        if value and paramnode.raw == "row":
            return "addtotals row"
    return "addtotals row"
    
def detect_truth_value(astring):
    value = False
    if astring.lower() in ["true", "t"]:
        value = True
    else:   
        try:
            value = float(valuenode.raw)
        except:
            pass
    return value
