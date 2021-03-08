from Client import *
from Constants import *

class Species:

    clients = RandomHashSet()
    representative = Client()
    score = 0

    def __init__(self, nRepresentative)
        self.representative = nRepresentative
        self.representative.setSpecies(self)
        self.clients.add(representative)

    def put(self,nClient):
        if(nClient.distance(self.representative)< cp):
            nClient.setSpecies(self)
            self.clients.add(representative)
            return True
        return False

    def force(self, nClient):
        nClient.setSpecies(self)
        self.clients.add(representative)

    def goExtinct(self):
        for a in self.clients.List:
            a.setSpecies(None)

    def evaluateScore(self):
        v = 0
        for a in self.clients.List:
            v+= a.getScore()
        self.score = v/self.clients.getSize()

    def reset(self, percentage):
        self.representative = clients.getRandom()

        self.goExtinct()

        self.clients.clear()
        self.clients.add(self.representative)
        self.representative.setSpecies(self)
        score=0

    def kill(self):
        self.clients.List.sort(reverse=True)

        for a in range(0, math.floor(percentage*self.clients.getSize())):
            self.clients.get(a).setSpecies(None)
            self.clients.delete(a)


    def breed(self):
        c1 = clients.getRandom()
        c2 = clients.getRandom()

        if(c1.getScore>=c2.getScore):
            return Genome.crossOver(c1.getGenome(), c2.getGenome())
        else:
            return Genome.crossOver(c2.getGenome(), c1.getGenome())

    def getSize(self):
        return self.clients.getSize()
