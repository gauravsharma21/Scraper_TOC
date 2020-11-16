from Info import Info
import re

class Tag:
    def __init__(self, props, parent, text, children):
        self.props = props
        self.text = text
        self.children = children
        self.parent = parent
        self.splitProps()

    def splitProps(self):
        if(self.props == None):
            return
        props = dict()
        arr = re.split(" ", self.props)
        props["tag"] = arr[0]
        for i in range(1, len(arr)):
            s = re.split("=", arr[i], 1)
            if(len(s) < 2):
                continue
            s[0].lstrip()
            s[0].rstrip()
            props[s[0]] = s[1]
        self.props = props

    def display(self, tabs = 0):
        if(self.props == None):
            return
        print("\t" * tabs , "props: ", self.props)
        print("\t" * tabs , "parent: ", self.parent)
        print("\t" * tabs , "Children: ")
        self.children.display(tabs + 1)

    def getString(self):
        return self.children.getString()

    def find(self, _tag):
        if(isinstance(self.children, Info)):
            return self.children.find(_tag)
        else:
            if(self.children.props["tag"] == _tag):
                return [self.children]
