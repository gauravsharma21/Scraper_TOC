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
        balance = 0
        cur = ""
        j = 0
        while(j < len(self.props) and self.props[j] != " "):
            cur += self.props[j]
            j += 1
        
        props["tag"] = cur
        cur = ""
        for i in range(j + 1, len(self.props)):
            if(self.props[i] == ' ' and balance == 0):
                s = re.split("=", cur)
                s[0] = s[0].lstrip()
                s[0] = s[0].rstrip()
                if(len(s) == 0 or len(s[0]) == 0):
                    continue
                elif(len(s) == 1):
                    props[s[0]] = True
                else:
                    props[s[0]] = s[1]
                cur = ""
            
            elif(self.props[i] == '"'):
                balance = balance ^ 1

            cur += self.props[i]
        
        if(len(cur) != 0):
            s = re.split("=", cur)
            s[0] = s[0].lstrip()
            s[0] = s[0].rstrip()
            if(len(s) == 0 or len(s[0]) == 0):
                p = 0    
            elif(len(s) == 1):
                props[s[0]] = True
            else:
                props[s[0]] = s[1]
            cur = ""
        self.props = props

    def display(self, tabs = 0):
        if(self.props == None):
            return
        print("\t" * tabs , "props: ", self.props)
        print("\t" * tabs , "parent: ", self.parent)
        print("\t" * tabs , "Children: ")
        if(self.children != None):
            self.children.display(tabs + 1)
        else:
            print("None")

    def getString(self):
        return self.children.getString()

    def find(self, _tag):
        if(isinstance(self.children, Info)):
            return self.children.find(_tag)
        else:
            if(self.children.props["tag"] == _tag):
                return [self.children]
