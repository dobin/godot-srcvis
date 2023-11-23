#!/usr/bin/python3

from typing import List
import os

from model import *
from parsing import *


projPath = "/mnt/c/Users/dobin/Repos/godot-helloworld/"


def walk():
    entries = {}
    for dirpath, dirs, files in os.walk(projPath):
        for filename in files:
            if "/addons/" in dirpath:
                continue
            if not (filename.endswith('.tscn') or filename.endswith('.gd')):
                continue

            filepath = os.path.join(dirpath, filename) 
            relpath = filepath.replace(projPath, "")

            filename_base = Path(filepath).stem
            if not filename_base in entries:
                entry: Entry = Entry()
                entry.rel_path = relpath
                entry.scene_filename = filepath
                entry.filename_base = filename_base
                entries[filename_base] = entry

            if filename.endswith('.tscn'): 
                parseSceneFile(filepath, relpath, entries[filename_base].entryScene)
            
            if filename.endswith(".gd"):
                if filename_base in entries:
                    parseGdscriptFile(filepath, relpath, entries[filename_base].entryGdscript)
                else:
                    parseGdscriptFile(filepath, relpath, None)
    return entries


def main():
    entries = walk()

    print()
    print("Output:")
    for basename, entry in entries.items():
        print("Basename: {}  Entry: {}".format(basename, entry.rel_path))

        print("  Scene:")
        for ext_resource in entry.entryScene.ext_resources:
            print("    ExtResource: {}".format(ext_resource.res))
        for node in entry.entryScene.nodes:
            print("    Node: {}".format(node.res))
        for subresource in entry.entryScene.sub_resources:
            print("    Getnodes: {}".format(subresource.res))
        for connection in entry.entryScene.connections:
            print("    Connection: {}".format(connection.res))

        print("  Gdscript:")
        for connect in entry.entryGdscript.connects:
            print("    Connect: {}".format(connect.res))
        for dollar in entry.entryGdscript.dollars:
            print("    Dollar: {}".format(dollar.res))
        for getnode in entry.entryGdscript.getnodes:
            print("    Getnode: {}".format(getnode.res))
        for load in entry.entryGdscript.loads:
            print("    load: {}".format(load.res))
        for preload in entry.entryGdscript.preloads:
            print("    preload: {}".format(preload.res))
        for new in entry.entryGdscript.news:
            print("    knew: {}".format(new.res))
        for instantiate in entry.entryGdscript.instantiates:
            print("    instantiate: {}".format(instantiate.res))


if __name__ == "__main__":
    main()
