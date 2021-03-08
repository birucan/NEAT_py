from Genome import *
from Species import *
from Calculator import *


class Client:

    genome = None
    score = 0
    species = None
    calculator = None

    def generateCalculator(self):
        self.calculator = Calculator(self.genome)

    def calculate(self,foo):
        if(self.calculator == None):
            if(self.genome == None):
                return
            else:
                generateCalculator()
        return self.calculator.calculate(foo)


    def distance(self, obj):
        return self.genome.distance(obj.genome)

    def mutate(self):
        self.genome.mutate()

    def getGenome(self):
        return self.genome

    def setGenome(self, nGen):
        self.genome= nGen


    def getScore(self):
        return self.score

    def setScore(self, nScore):
        self.score= nScore


    def getSpecies(self):
        return self.species

    def setSpecies(self, nSpecies):
        self.species= nSpecies

    def getCalculator(self)
        return self.calculator


    def __eq__(self, obj):
        return (self.score==obj.score)


    def __lt__(self, obj):
        return (self.score< obj.score)


    def __gt__(self, obj):
        return (self.score > obj.score)
