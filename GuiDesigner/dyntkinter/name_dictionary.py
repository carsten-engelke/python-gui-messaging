class GuiDictionary:

    def __init__(self): self.elements = {}

    def setElement(self,name,thisone):
        if not name in self.elements: self.elements[name] = [thisone]
        else: self.elements[name].append(thisone)

    def getEntry(self,name,nr=0):
        if name in self.elements: return self.elements[name][nr]
        return None

    def getChildrenList(self):
        element_list = []
        for name,entry in self.elements.items():
            for x in entry: element_list.append(x)
        return element_list

    def getEntryByStringAddress(self,refstring):
        for name,entry in self.elements.items():
            for x in entry:
                if str(x) == refstring: return x
        return None

    def getNameAndIndex(self,reference):
        for name,entry in self.elements.items():
            for index in range(len(entry)):
                if entry[index] == reference:
                    if len(entry) == 1: return (name,-1)
                    else: return (name,index)
        return (None,None)

    def getNameAndIndexByStringAddress(self,reference_string):
        for name,entry in self.elements.items():
            for index in range(len(entry)):
                if str(entry[index]) == reference_string:
                    if len(entry) == 1: return (name,-1)
                    else: return (name,index)
        return (None,None)