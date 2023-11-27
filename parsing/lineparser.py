from parsing.utils import *


def parse_line_signal(line):
    return line
    #return line[line.index(" "):]

def parse_line_connect(line):
    return line

def parse_line_dollar(line):
    dollar_strings = extract_dollar_strings(line)
    return line[:first_non_alpha_offset(line)]
    if False:
        if len(dollar_strings) > 0:
            ds = dollar_strings[0].split(".")
            ds = ds[0]
            return ds
            #if not any(mystr.res == ds for mystr in entryGdscript.dollars):
            #    entryGdscript.dollars.append(MyStr(line, ds))


def parse_line_load(line):
    return cut_from_to(line, 'load(', ')')

def parse_line_preload(line):
    return cut_from_to(line, 'preload("', '")')

def parse_line_new(line):
    return find_word_before_string(line, ".new(")

def parse_line_instantiate(line):
    return find_word_before_string(line, ".instantiate(")

def parse_line_emit(line):
    return find_word_before_string(line, ".emit(")

def parse_line_get_node_in_group(line):
    return cut_from_to(line, 'get_nodes_in_group("', '")')

def parse_line_export(line):
    sa = line.split(" ")
    return "{}: {}".format(sa[2], sa[3])
