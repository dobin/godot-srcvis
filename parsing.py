from utils import *
from pathlib import Path

from model import *


def parseSceneLine(line, entryScene: EntryScene):
    if not line.startswith("["):
        return
    #print("Line: {}".format(line))
    line = line.strip()
    line = line.replace("[", "")
    line = line.replace("]", "")
    lineDict = parse_key_value_string(line)

    if lineDict["meta"] == "ext_resource":
        s = "{}".format(
            lineDict["path"],
        )
        entryScene.ext_resources.append(MyStr(line, s))

    elif lineDict["meta"] == "node":
        if 'type' in lineDict:
            s = "{}: {}".format(
                lineDict["name"],
                lineDict["type"],
            )
            entryScene.nodes.append(MyStr(line, s))
        elif 'ExtResource' in lineDict:
            s = "{}: {}".format(
                lineDict["name"],
                lineDict["ExtResource"],
            )
            entryScene.ext_resources.append(MyStr(line, s))
    elif lineDict["meta"] == "sub_resource":
        s = "{}".format(
            lineDict["type"],
        )
        entryScene.sub_resources.append(MyStr(line, s))
    elif lineDict["meta"] == "connection":
        s = "{}:{} ->{}:{}".format(
            lineDict["from"],
            lineDict["signal"],
            lineDict["to"],
            lineDict["method"],
        )
        entryScene.connections.append(MyStr(line, s))


def parseSceneFile(filepath, relpath, entryScene):
    print("Parse: {} {}".format(filepath, relpath))

    file = open(filepath, 'r')
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        parseSceneLine(line, entryScene)
    

####################


def parseGdscriptFile(filepath, relpath, entryGdscript: EntryGdscript):
    print("Parse: {} {}".format(filepath, relpath))

    file = open(filepath, 'r')
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        parseGdscriptLine(line, entryGdscript)


def parseGdscriptLine(line, entryGdscript):
    line = line.strip()

    if '.connect(' in line:
        #print("---> {}".format(line))
        entryGdscript.connects.append(MyStr(line, line))
    if '$' in line:
        dollar_strings = extract_dollar_strings(line)
        entryGdscript.dollars.append(MyStr(line, " ".join(dollar_strings)))
        #print("---> {} / $:{}".format(line, dollar_strings))
    if 'get_node' in line:
        x = line[line.find('get_node'):]
        entryGdscript.getnodes.append(MyStr(line, x))
        #print("---> {} / gn:{}".format(line, x))
    if 'load(' in line:
        x = line[line.find('load'):]
        entryGdscript.loads.append(MyStr(line, x))
        #print("---> {} / l:{}".format(line, x))
    if 'preload(' in line:
        x = line[line.find('preload'):]
        #print("---> {} / p:{}".format(line, x))
        entryGdscript.preloads.append(MyStr(line, x))
    if 'new(' in line:
        x = find_word_before_string(line, "new(")
        #print("---> {} / n:{}".format(line, x))
        entryGdscript.news.append(MyStr(line, x))
    if 'instantiate(' in line:
        x = find_word_before_string(line, "instantiate(")
        entryGdscript.instantiates.append(MyStr(line, x))
        #print("---> {} / i:{}".format(line, x))
        #print("---> {}".format(line))
