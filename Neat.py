from Constants import *
from ConnectionGene import *
from NodeGene import *
from Genome import *
from DataStructures.RandomHashSet import *


class Neat:

    allConections = {}
    allNodes = RandomHashSet()

    inputSize =-1
    outputSize =-1
    clients =-1

    def __init__(self, inputSize, outputSize, clients):
        self.reset(inputSize, outputSize, clients)

    def emptyGenome(self):
        nGenome = Genome(self)

        for a in range(0, self.inputSize + self.outputSize):
            nGenome.getNodes().add(self.getNodeId(a+1))

        return nGenome

    def reset(self, ninputSize, noutputSize, nclients):
        self.inputSize= ninputSize
        self.outputSize = noutputSize
        self.clients = nclients

        self.allConections.clear()
        self.allNodes.clear()

        for a in range(0, self.inputSize):
            nNode = self.getNode()

            nNode.setX(0.1)
            nNode.setY((a+1)/self.inputSize+1)

        for b in range(0, self.outputSize):
            nNode = self.getNode()

            nNode.setX(0.9)
            nNode.setY((b+1)/self.outputSize+1)


    def getNode(self):
        nNode= NodeGene(self.allNodes.getSize()+1)
        self.allNodes.add(nNode)
        return nNode

    def getNodeId(self, id):
        if(id<= self.allNodes.getSize()):
            return self.allNodes.get(id-1);
        else:
            return getNode();

def main():
    nNeat = Neat(3,3,100)

    nGenome = nNeat.emptyGenome()
    print(nGenome.getNodes().getSize())
    print(nGenome.getNodes().Dict)

if __name__ == '__main__':
    main()
