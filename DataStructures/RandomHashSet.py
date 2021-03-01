import random

class RandomHashSet:
    List = []
    Dict = {}

    def contains(self, obj):
        if(obj in self.Dict):
            return True
        else:
            return False

    def getRandom(self):
        if(self.len(self.Dict)>0):
            return random.choice(list(self.Dict.values()))

    def getSize(self):
        return len(self.Dict)

    def add(self, obj):
        if(not self.contains(obj)):
            self.Dict[obj] = obj;
            self.List.append(obj);
            return True
        else:
            return False

    def delete(self, index):
        if(index < 0 or index >= len(List)):
            return False;
        else:
            del self.Dict[self.List[index]]
            self.List.remove(self.List[index])
            return True;

    def deleteObj(self, obj):
        if(self.Dict.contains(obj)):
            del self.Dict[obj]
            self.List.remove(obj)
            return True;
        else:
            return False;



    def clear(self):
        self.List = []
        self.Dict = {}

    def get(self, index):
        if(index < 0 or index >= len(self.List)):
            return self.List[index]
