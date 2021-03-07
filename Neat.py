from Constants import *
from ConnectionGene import *
from NodeGene import *
from Genome import *
from DataStructures.RandomHashSet import *
from GUI import *


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

            #print("input node x,y:  "+str(nNode.getX())+" , "+str(nNode.getY()))

        for b in range(0, self.outputSize):
            nNode = self.getNode()
            nNode.setX(0.9)
            nNode.setY((b+1)/self.outputSize+1)
            #print("output node x,y:  "+str(nNode.getX())+" , "+str(nNode.getY()))

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

    def getConnection(self, node1, node2):
        nCon= ConnectionGene(node1, node2)

        if(len(self.allConections)==0):
            nCon.setInnovationNum(1)
            self.allConections[nCon.hashCode()] = nCon
            return nCon
        elif(self.allConections.get(nCon.hashCode())):
            print(str(nCon.getOrigin().getInnovationNum())+" to "+str(nCon.getTarget().getInnovationNum())+" is in connections")
            nCon.setInnovationNum(self.allConections.get(nCon.hashCode()).getInnovationNum())
            return nCon
        else:
            nCon.setInnovationNum(len(self.allConections)+1)
            self.allConections[nCon.hashCode()] = nCon

        return nCon








def main():
    nNeat = Neat(2,2,100)


    nGenome = nNeat.emptyGenome()
    b=0
    nodosRandom= 0
    while(b<nodosRandom):
        nX=random.random()
        if(nX>=0.2 and nX<=0.8):
            nNodeGene = NodeGene(-1)
            nNodeGene.setX(nX)
            nNodeGene.setY(random.choice(nGenome.getNodes().List).getY())
            nGenome.nodes.add(nNodeGene)
            b=b+1


    a=0
    connections=0
    while(a<connections):


        b= nGenome.getNodes().getRandom()
        c= nGenome.getNodes().getRandom()

        if(b.getX()!=c.getX()):
            con= ConnectionGene(b,c)
            #con.setWeight(random.random()*10)
            if(nGenome.connections.add(con)):
                a=a+1
            elif(not nGenome.connections.add(con)):

                a=connections
        else:
            pass






    gui = GUI(nGenome,10)



if __name__ == '__main__':
    main()
