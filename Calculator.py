from Genome import *
from DataStructures.RandomHashSet import *
from Connection import *
import time


class Calculator:

    inputNodes = []
    hiddenNodes = []
    outputNodes = []
    nodeDict = {}

    def __init__(self, nGen):
        #re innitialized lists and Dict to make them unique to each object
        self.inputNodes = []
        self.hiddenNodes = []
        self.outputNodes = []
        self.nodeDict = {}

        nodes = nGen.getNodes()
        cons = nGen.getConnections()



        for a in nodes.List:
            nNode = Node(a.getX())
            self.nodeDict[a.getInnovationNum()]= nNode

            if(a.getX()<=0.1):
                self.inputNodes.append(nNode)
            elif(a.getX()>=0.9):
                self.outputNodes.append(nNode)
            else:
                #print("added hiddenNode "+str(nNode.getX()))
                self.hiddenNodes.append(nNode)


        #ts = time.time()
        #self.hiddenNodes.sort()
        #ts2 = time.time()
        #print("time to sort: "+str(ts2-ts))

        for b in cons.List:
            origin = b.getOrigin()
            target = b.getTarget()

            nOrg = self.nodeDict[origin.getInnovationNum()]
            nTar = self.nodeDict[target.getInnovationNum()]

            nCon = Connection(nOrg, nTar)
            nCon.setWeight(b.getWeight())
            nCon.setEnabled(b.isEnabled())

            nTar.getConnections().append(nCon)

    def calculate(self, input):
        if(len(input) != len(self.inputNodes)):
            print("not equal data")

        output=[]
        for a in range(0, len(self.inputNodes)):
            self.inputNodes[a].setOutput(input[a])

        for b in self.hiddenNodes:
            b.calculate()

        for c in range(0, len(self.outputNodes)):
            self.outputNodes[c].calculate()
            output.append(self.outputNodes[c].getOutput())

        #print(output)
        return output
