from DataStructures.RandomHashSet import *
from Constants import *
from ConnectionGene import *
from Calculator import *
import random
import math

class Genome:

    connections = RandomHashSet();
    nodes = RandomHashSet();
    neat = ''
    calculator = ''

    #TODO get rid of calculator in genome
    def generateCalculator(self):
        self.calculator = Calculator(self)

    def calculate(self,foo):
        if(self.calculator!=''):
            return self.calculator.calculate(foo)
        else:
            return null

    def distance(self, g2):
        g1 = self

        #indexes
        iG1=0
        iG2=0
        disjoint=0
        excess = 0
        weightDiff = 0
        similar = 0

        lastInnovation1=0
        lastInnovation2=0

        if(g1.getConnections().getSize()!=0):
            lastInnovation1 = g1.getConnections().get(g1.getConnections.size-1).getInnovationNum()
        if(g2.getConnections().getSize()!=0):
            lastInnovation2 = g2.getConnections().get(g2.getConnections.size-1).getInnovationNum()

        if(lastInnovation1<lastInnovation2):
            ge= g1
            g1 = g2
            g2 = ge

        while((iG1 < g1.getConnections().getSize()) and (iG2 < g2.getConnections().getSize())):

            gene1 = g1.getConnections().get(iG1)
            gene2 = g2.getConnections().get(iG2)

            #inovation numbers
            inn1 = gene1.getInnovationNum()
            inn2 = gene2.getInnovationNum()

            #similar
            if(inn1==inn2):
                iG1=iG1+1;
                iG2=iG2+1;
                similar = similar +1
                weightDiff += math.abs(gene1.getWeight()-gene2.getWeight())


            #disjoints
            if(inn1>inn2):
                iG2=iG2+1;
                disjoint=disjoint+1

            if(inn1<inn2):
                iG1=iG1+1
                disjoint=disjoint+1


        weightDiff = weightDiff/similar
        excess = g1.getConnections().getSize() - iG1

        N = max(g1.getConnections().size(), g2.getConnections().size())

        if(N<20):
            N=1

        return ((c1 * disjoint/N)+(c2 * excess/N)+ (c3 * excess/N) )


    def __init__(self, nNeat):
        #print(self.connections.List is self.nodes.List)
        self.neat = nNeat


    def crossOver(self, g1, g2):
        g1 = self

        childGenome =  g1.getNeat().EmptyGenome()

        #indexes
        iG1=0
        iG2=0

        while((iG1 < g1.getConnections().getSize()) and (iG2 < g2.getConnections().getSize())):

            gene1 = g1.getConnections().get(iG1)
            gene2 = g2.getConnections().get(iG2)

            #inovation numbers
            inn1 = gene1.getInnovationNum()
            inn2 = gene2.getInnovationNum()

            if(inn1==inn2):

                choice =  random.choice((gene1,gene2))
                childGenome.getConnections().add(g1.getNeat().getConnection(choice))

                iG1=iG1+1;
                iG2=iG2+1;

            if(inn1>inn2):
                iG2=iG2+1;

            if(inn1<inn2):
                iG1=iG1+1
                childGenome.getConnections().add(g1.getNeat().getConnection(gene1))

        while(iG1< g1.getConnections.getSize()):
            gene1 = g1.getConnections().get(IG1)
            childGenome.getConnections().add(g1.getNeat().getConnection(gene1))
            iG1=iG1+1

        for CG in childGenome.getConnections().getData():
            childGenome.getNodes().add(CG.getOrigin())
            childGenome.getNodes().add(CG.getTarget())

        return childGenome



    #TODO mutate
    def mutate(self):
        if(PROBABILITY_MUTATE_LINK>random.random()):
            self.mutateLink()
        if(PROBABILITY_MUTATE_NODE>random.random()):
            self.mutateNode()
        if(PROBABILITY_MUTATE_TOGGLE_LINK>random.random()):
            self.mutateToggleLink()
        if(PROBABILITY_MUTATE_WEIGHT_SHIFT>random.random()):
            self.mutateWeightShift()
        if(PROBABILITY_MUTATE_WEIGHT_RANDOM>random.random()):
            self.mutateWeightRandom()


    def mutateLink(self):
        for a in range(0, MUTATION_LINK_ATTEMPS):

            nodeA =  self.getNodes().getRandom()
            nodeB =  self.getNodes().getRandom()
            con = None

            if(nodeA.getX()==nodeB.getX()):
                continue

            if(nodeA.getX()<nodeB.getX()):
                con = ConnectionGene(nodeA,nodeB)
            else:
                con = ConnectionGene(nodeB,nodeA)


            if(self.getConnections().contains(con)):
                continue


            con = self.neat.getConnection(con.getOrigin(), con.getTarget())

            con.setWeight((random.random() * 2-1)*WEIGHT_RANDOM_STRENGTH)
            self.connections.addSorted(con)

            break


    def mutateNode(self):
        con = self.getConnections().getRandom()


        if(con== None):
            return

        origin = con.getOrigin()
        target = con.getTarget()
        middle = self.neat.getNode()

        signo = 1
        if ( random.random()>0.5):
            signo=-1

        middle.setX((origin.getX()+target.getX())/2)
        middle.setY(((origin.getY()+target.getY())/2)+(signo*(random.random()*0.075)))

        con1 = self.neat.getConnection(origin, middle)
        con2 = self.neat.getConnection(middle, target)


        con1.setWeight(1)
        con2.setWeight(con.getWeight())
        con2.setEnabled(con.isEnabled())

        self.nodes.add(middle)
        self.connections.deleteObj(con)
        self.connections.add(con1)
        self.connections.add(con2)







    def mutateToggleLink(self):
        nCon = self.getConnections().getRandom()

        if(nCon != None):
            nCon.toggle()

    def mutateWeightShift(self):
        nCon = self.getConnections().getRandom()

        if(nCon != None):
            nCon.setWeight(nCon.getWeight()+(random.random()*2-1)*WEIGHT_SHIFT_STRENGTH)


    def mutateWeightRandom(self):
        nCon = self.getConnections().getRandom()

        if(nCon != None):
            nCon.setWeight((random.random()*2-1)*WEIGHT_RANDOM_STRENGTH)

    def getConnections(self):
        return self.connections

    def getNodes(self):
        return self.nodes
