
class Entry():
    def __init__(self):
        self.rel_path = ""
        self.scene_filename = ""
        self.gdscript_filename = ""
        self.filename_base = ""

        self.entryScene = EntryScene()
        self.entryGdscript = EntryGdscript()


class EntryScene():
    def __init__(self):
        # Scene file
        self.ext_resources = []
        self.nodes = []
        self.sub_resources = []
        self.connections = []
        

class EntryGdscript():
    def __init__(self):
        # GDScript file
        self.connects = []
        self.dollars = []
        self.getnodes = []
        self.loads = []
        self.preloads = []
        self.news = []
        self.instantiates = []
        self.signals = []


class MyStr():
    def __init__(self, orig, res):
        self.orig = orig
        self.res = res
