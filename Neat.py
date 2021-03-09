from Constants import *
from ConnectionGene import *
from NodeGene import *
from Genome import *
from DataStructures.RandomHashSet import *
from DataStructures.RandomSelector import *
from GUI import *
from Client import *
from Species import *
from Calculator import *

class Neat:

    allConections = {}
    allNodes = RandomHashSet()

    clients =  RandomHashSet()
    species =  RandomHashSet()


    inputSize =-1
    outputSize =-1
    clientSize =-1



    def __init__(self, ninputSize, noutputSize, nclientSize):
        self.reset(ninputSize, noutputSize, nclientSize)

    def emptyGenome(self):
        nGenome = Genome(self)


        for a in range(0, self.inputSize + self.outputSize):
            nGenome.getNodes().add(self.getNodeId(a+1))
        return nGenome


    def reset(self, ninputSize, noutputSize, nclients):
        self.inputSize= ninputSize
        self.outputSize = noutputSize
        self.clientSize = nclients

        self.allConections.clear()
        self.allNodes.clear()
        self.clients.clear()

        for a in range(0, self.inputSize):

            nNode = self.getNode()
            nNode.setX(0.1)
            nNode.setY((a+1)/self.inputSize+1)

            #print("input node x,y:  "+str(nNode.getX())+" , "+str(nNode.getY()))

        for b in range(0, self.outputSize):

            nNode = self.getNode()
            nNode.setX(0.9)
            nNode.setY((b+1)/self.outputSize+1)
            #print("output node x,y:  "+str(nNode.getX())+" , "+str(nNode.getY()))

        for c in range(0, self.clientSize):
            nCli = Client()
            nCli.setGenome(self.emptyGenome())
            nCli.generateCalculator()
            self.clients.add(nCli)
        print(self.clients.getSize())

    def getClient(self, ind):
        return clients.get

    #Creates new node, adds it to node list and returns said node
    def getNode(self):
        nNode= NodeGene(self.allNodes.getSize()+1)
        self.allNodes.add(nNode)
        return nNode

    def getNodeId(self, id):
        #print("id, getNodes.size  :"+str(id)+"  "+str(self.allNodes.getSize()))

        if(id<= self.allNodes.getSize()):
            return self.allNodes.get(id-1);


        return getNode();

    #def getConnectionSelf(self, node):


    def getConnection(self, node1, node2):
        nCon= ConnectionGene(node1, node2)

        if(len(self.allConections)==0):
            nCon.setInnovationNum(1)
            self.allConections[nCon.hashCode()] = nCon
            return nCon
        elif(self.allConections.get(nCon.hashCode())):
            #print(str(nCon.getOrigin().getInnovationNum())+" to "+str(nCon.getTarget().getInnovationNum())+" is in connections")
            nCon.setInnovationNum(self.allConections.get(nCon.hashCode()).getInnovationNum())
            return nCon
        else:
            nCon.setInnovationNum(len(self.allConections)+1)
            self.allConections[nCon.hashCode()] = nCon

        return nCon

    def generateSpecies(self):

        for s in self.species.List:
            s.reset()

        for c in self.clients.List:
            if(c.getSpecies() is not None):
                print(c.getSpecies())
                continue

            found = False
            for s in self.species.List:
                if(s.put(c)):
                    #print(found)
                    found = True
                    break
            if(not found):
                self.species.add(Species(c))

        for s in self.species.List:
            s.evaluateScore()

    def kill(self):
        for s in self.species.List:
            s.kill(1-SURVIVORS)

    def removeExtinctSpecies(self):
        #print(self.species)
        #print(self.species.getSize())

        for a in range(self.species.getSize()-1,0):
            if(self.species.get(a).getSize()<=1):
                self.species.get(a).goExtinct()
                self.species.delete(a)

    def reproduce(self):
        selector = RandomSelector()
        for s in self.species.List:
            selector.add(s,s.score)

        for c in self.clients.List:
            #print(c)
            s = selector.getRandom()
            #print(s)
            c.setGenome(s.breed())
            s.force(c)

    def mutate(self):
        for c in self.clients.List:
            c.mutate()



    def evolve(self):
        self.generateSpecies()
        self.kill()
        self.removeExtinctSpecies()
        self.reproduce()
        self.mutate()

        for a in self.clients.List:
            a.generateCalculator()

    def showSpecies(self):
        print("_._._._._._._._._._._._._._._._._._")
        #print(len(self.species.List[0].clients.List))
        for a in self.species.List:
            print(str(a)+" score: "+str(a.score)+" size: "+str(a.clients.getSize()))




def main2():
    nNeat =  Neat(10,1,1000)

    ina = [None]*10

    for a in range (0,len(ina)):
        ina[a]= random.Random()


    for a in range(0,100):
        for b in nNeat.clients.List:
            score = b.calculate(ina)[0];
            b.setScore(score)

        nNeat.evolve()
        nNeat.showSpecies()
        #gui = GUI(nNeat.clients.get(0).genome,5)


main2()
#if __name__ == '__main__':
#    main()
