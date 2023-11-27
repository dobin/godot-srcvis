from parsing.utils import *


from parsing.lineparser import *
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

    if line.startswith("#"):
        return

    if line.startswith("signal "):
        x = parse_line_signal(line)
        entryGdscript.signals.append(MyStr(line, x))
    if '.connect(' in line:
        x = parse_line_connect(line)
        entryGdscript.connects.append(MyStr(line, x))
    if '$' in line:
        x = parse_line_connect(line)
        entryGdscript.dollars.append(MyStr(line, x))  # doubles
    if '.get_nodes_in_group' in line:
        x = parse_line_get_node_in_group(line)
        entryGdscript.getnodes.append(MyStr(line, x))
    if '.load(' in line:
        x = parse_line_load(line)
        entryGdscript.loads.append(MyStr(line, x))
    if '.preload(' in line:
        x = parse_line_preload(line)
        entryGdscript.preloads.append(MyStr(line, x))
    if '.new(' in line:
        x = parse_line_new(line)
        entryGdscript.news.append(MyStr(line, x))
    if '.instantiate(' in line:
        x = parse_line_instantiate(line)
        entryGdscript.instantiates.append(MyStr(line, x))
    if '.emit(' in line:
        x = parse_line_emit(line)
        entryGdscript.emits.append(MyStr(line, x))
    if '@export' in line:
        x = parse_line_export(line)
        entryGdscript.exports.append(MyStr(line, x))
