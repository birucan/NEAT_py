from Client import *
from Constants import *

class Species:

    clients = RandomHashSet()
    representative = None
    score = 0

    def __init__(self, nRepresentative):
        self.representative = nRepresentative
        self.representative.setSpecies(self)
        self.clients.add(self.representative)

    def put(self,nClient):
        if(nClient.distance(self.representative)< cp):
            nClient.setSpecies(self)
            self.clients.add(self.representative)
            return True
        return False

    def force(self, nClient):
        nClient.setSpecies(self)
        self.clients.add(self.representative)

    def goExtinct(self):
        for a in self.clients.List:
            a.setSpecies(None)

    def evaluateScore(self):
        v = 0
        for a in self.clients.List:
            v+= a.getScore()
        self.score = v/self.clients.getSize()

    def reset(self):
        self.representative = self.clients.getRandom()

        self.goExtinct()

        self.clients.clear()
        self.clients.add(self.representative)
        self.representative.setSpecies(self)
        score=0

    def kill(self, percentage):
        self.clients.List.sort(reverse=True)
        foo = math.floor(percentage*self.clients.getSize())
        for a in range(0, foo):
            self.clients.get(a).setSpecies(None)
            self.clients.delete(a)


    def breed(self):
        c1 = self.clients.getRandom()
        c2 = self.clients.getRandom()

        if(c1.getScore()>=c2.getScore()):
            return Genome(super).crossOver(c1.getGenome(), c2.getGenome())
        else:
            return Genome(super).getGenome().crossOver( c1.getGenome(),c1.getGenome())

    def getSize(self):
        return self.clients.getSize()

    def hashCode(self):
        return self.score*31+self.getSize()*31
