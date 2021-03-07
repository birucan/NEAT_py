import random

class RandomHashSet:
    List = []
    Dict = {}

    def __init__(self):
        self.List = []
        self.Dict = {}


    def contains(self, obj):
        #TODO find better solution for stupid workaround
        if(obj.hashCode() in self.Dict):
            return True
        else:
            return False

    def getRandom(self):
        if(len(self.Dict)>0):
            return random.choice(list(self.Dict.values()))

    def getSize(self):
        return len(self.Dict)

    def add(self, obj):
        if(not self.contains(obj)):
            self.Dict[obj.hashCode()] = obj;
            self.List.append(obj);
            #print(self.Dict)
            return True
        else:
            return False

    def delete(self, index):
        if(index < 0 or index >= len(List)):
            return False;
        else:
            del self.Dict[self.List[index].hashCode()]
            self.List.remove(self.List[index])
            return True;

    def deleteObj(self, obj):
        if(self.Dict.get(obj.hashCode())):

            del self.Dict[obj.hashCode()]


            self.List.remove(obj)

            return True;
        else:
            return False;



    def clear(self):
        self.List = []
        self.Dict = {}

    def get(self, index):
        if( not index < 0 or index >= len(self.List)):
            #print(self.List[index])
            return self.List[index]

    def addSorted(self, obj):
        if(len(self.List)==0):
            self.List.append(obj)
            self.Dict[obj.hashCode()]=obj
        else:
            for a in range (0,len(self.List)):
                innovation = self.List[a].getInnovationNum()

                if(obj.getInnovationNum()>innovation and not self.contains(obj)):
                    self.Dict[obj.hashCode()] = obj
                    self.List.insert(a, obj)
                    return
