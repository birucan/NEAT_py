from Gene import *

class NodeGene(Gene):

    x=-1;
    y=-1;

    #def __init__(self, pInnovationNum):
    #    super(pInnovationNum)

    def getX(self):
        return self.x

    def setX(self, nX):
        self.x=nX

    def getY(self):
        return self.y

    def setY(self, nY):
        self.y=nY

    def equals(self, obj):
        if(not isinstance(obj, NodeGene)):
            return False

        return self.innovationNum==obj.getInnovationNum()

    def hashCode(self):
        return self.innovationNum

def tester():

    test = NodeGene(1)
    test.setX(2)
    test.setY(3)


    test2 = NodeGene(1)
    test.setX(4)
    test.setY(6)

    foo ="foo"
    print(test.equals(test2))
    print(test.equals(foo))

#tester()
