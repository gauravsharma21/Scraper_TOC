import re

class Info:
    def __init__(self, strings, tags, parent):
        self.strings = strings
        self.tags = tags
        self.parent = parent

    def display(self, tabs = 0):
        print("\t" * tabs , "parent: ", self.parent)
        print("\t" * tabs , "text: ",self.strings)
        print("\t" * tabs , "tags: ")
        for tag in self.tags:
            tag.display(tabs + 1)

    def getString(self):
        return self.strings

    def find(self, _tag):
        output = []
        for tag in self.tags:
            if(tag.props["tag"] == _tag):
                output.append(tag)
        return output
