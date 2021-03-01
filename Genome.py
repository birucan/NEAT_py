from DataStructures.RandomHashSet import *
from Constants import *
import random

class Genome:

    connections = RandomHashSet();
    nodes = RandomHashSet();
    neat = ''
    #TODO distance
    def distance(self, g1, g2):
        return 1;

    def __init__(self, nNeat):
        self.neat = nNeat

    #TODO crossover
    def crossOver(self, g1, g2):
        return 1;

    #TODO mutate
    def mutate(self):
        return "f";

    def getConnections(self):
        return self.connections

    def getNodes(self):
        return self.nodes
