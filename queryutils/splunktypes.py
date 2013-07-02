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

audit_command = Type("InputtingSelection", "audit")
audit_command.set_attributes(["inputs_metadata"])
implemented_commands.append(audit_command)

bucket_command = Type("TransformingProjection", "bucket")
bucket_command.set_attributes(["function_of_other_rows",
                                "numeric_domain",
                                "range_domain"])
implemented_commands.append(bucket_command)

chart_command = Type("Aggregation", "chart")
chart_command.set_attributes(["visualization_component"])
implemented_commands.append(chart_command)

sichart_command = Type("Aggregation", "sichart")
sichart_command.set_attributes(["visualization_component"])
implemented_commands.append(sichart_command)

collect_command = Type("Meta", "collect")
collect_command.set_attributes(["outputs_data"])
implemented_commands.append(collect_command)

convert_command = Type("TransformingProjection", "convert")
convert_command.set_attributes(["function_of_same_row",
                                    "string_domain",
                                    "numeric_range"])
implemented_commands.append(convert_command)

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

export_command = Type("Meta", "export")
export_command.set_attributes(["outputs_data"])
implemented_commands.append(export_command)

extract_command = Type("ExtendedProjection", "extract")
extract_command.set_attributes(["string_function",
                                    "function_of_multiple_columns",
                                    "multiple_columns_added",
                                    "data_dependent_num_columns_added"])
implemented_commands.append(extract_command)

kv_command = Type("ExtendedProjection", "kv")
kv_command.set_attributes(["string_function",
                                    "function_of_multiple_columns",
                                    "multiple_columns_added",
                                    "data_dependent_num_columns_added"])
implemented_commands.append(kv_command)

fields_command = Type("Projection", "fields")
implemented_commands.append(fields_command)

fieldformat_command = Type("TransformingProjection", "fieldformat")
fieldformat_command.set_attributes(["function_of_same_row",
                                        "string_domain",
                                        "string_range"])
implemented_commands.append(fieldformat_command)

fillnull_command = Type("TransformingProjection", "fillnull")
fillnull_command.set_attributes(["function_of_same_row", 
                                    "null_domain", 
                                    "user_defined_range"])
implemented_commands.append(fillnull_command)

inputlookup_command = Type("InputtingSelection", "inputlookup")
inputlookup_command.set_attributes(["inputlookup"])
implemented_commands.append(inputlookup_command)

inputcsv_command = Type("InputtingSelection", "inputcsv")
inputcsv_command.set_attributes(["inputcsv"])
implemented_commands.append(inputcsv_command)

head_command = Type("FilterSelection", "head")
head_command.set_attributes(["by_index"])
implemented_commands.append(head_command)

localop_command = Type("Meta", "localop")
localop_command.set_attributes(["controls_computation"])
implemented_commands.append(localop_command)

lookup_command = Type("Join", "lookup")
implemented_commands.append(lookup_command)

macro_command = Type("Macro", "macro")
implemented_commands.append(macro_command)

makemv_command = Type("TransformingProjection", "makemv")
makemv_command.set_attributes(["function_of_same_row",
                                "string_domain"])
implemented_commands.append(makemv_command)

multikv_command = Type("TransformingProjection", "multikv")
multikv_command.set_attributes(["string_domain",
                                "string_range"])
implemented_commands.append(multikv_command)

mvexpand_command = Type("InputtingSelection", "mvexpand")
mvexpand_command.set_attributes(["inputs_from_current_data"])
implemented_commands.append(mvexpand_command)

outputlookup_command = Type("Meta", "outputlookup")
outputlookup_command.set_attributes(["outputs_data"])
implemented_commands.append(outputlookup_command)

overlap_command = Type("Miscellaneous", "overlap")
implemented_commands.append(overlap_command)

rare_command = Type("Aggregation", "rare")
rare_command.set_attributes(["reorders",
                                "applies_fixed_function"])
implemented_commands.append(rare_command)

sirare_command = Type("Aggregation", "sirare")
sirare_command.set_attributes(["reorders",
                                "applies_fixed_function"])
implemented_commands.append(sirare_command)

regex_command = Type("FilterSelection", "regex")
regex_command.set_attributes(["by_user_string_match"])
implemented_commands.append(regex_command)

relevancy_command = Type("ComplexAggregation", "relevancy")
implemented_commands.append(relevancy_command)

rename_command = Type("Rename", "rename")
implemented_commands.append(rename_command)

replace_command = Type("TransformingProjection", "replace")
replace_command.set_attributes(["function_of_same_row",
                                    "string_domain",
                                    "string_range"])
implemented_commands.append(replace_command)

reverse_command = Type("Reorder", "reverse")
implemented_commands.append(reverse_command)

rex_command = Type("ExtendedProjection", "rex")
rex_command.set_attributes(["string_function",
                            "function_of_single_columns",
                            "multiple_columns_added"])
implemented_commands.append(rex_command)

search_command = Type("FilterSelection", "search")
search_command.set_attributes(["by_user_string_match",
                                "by_boolean_statement"])
implemented_commands.append(search_command)

sort_command = Type("Reorder", "sort")
implemented_commands.append(sort_command)

strcat_command = Type("ExtendedProjection", "strcat")
strcat_command.set_attributes(["string_function",
                                "function_of_multiple_columns"])
implemented_commands.append(strcat_command)

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

stats_command = Type("Aggregation", "stats")
implemented_commands.append(stats_command)

sistats_command = Type("Aggregation", "sistats")
implemented_commands.append(sistats_command)

sitimechart_command = Type("Aggregation", "sitimechart")
sitimechart_command.set_attributes(["visualization_component"])
implemented_commands.append(sitimechart_command)

top_command = Type("Aggregation", "top")
top_command.set_attributes(["reorders",
                                "applies_fixed_function"])
implemented_commands.append(top_command)

sitop_command = Type("Aggregation", "sitop")
sitop_command.set_attributes(["reorders",
                                "applies_fixed_function"])
implemented_commands.append(sitop_command)

transpose_command = Type("Transpose", "transpose")
implemented_commands.append(transpose_command)

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
#print [str(c) for c in implemented_commands]
   
names = [c.name for c in implemented_commands]
types = [c.typestr for c in implemented_commands]
command_type_lookup = dict(zip(names, types))

