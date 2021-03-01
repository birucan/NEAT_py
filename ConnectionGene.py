from Gene import *
from NodeGene import *
from Constants import *

class ConnectionGene():

    origin = NodeGene(-1)
    target = NodeGene(-1)

    weight=-1;
    enabled = True

    def __init__(self, nOrigin, nTarget):
        self.origin = nOrigin
        self.target = nTarget

    def getOrigin(self):
        return self.origin

    def setOrigin(self, nOrigin):
        self.origin = nOrigin

    def getTarget(self):
        return self.target

    def setTarget(self, nTarget):
        self.target = ntarget

    def getWeight(self):
        return self.weight

    def setWeight(self, nWeight):
        self.origin = nWeight

    def isEnabled(self):
        return self.enabled

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def equals(self, obj):
        if(not isinstance(obj, NodeGene)):
            return False

        return (self.origin==obj.getOrigin() & self.target==obj.getTarget())

    def hashCode(self):
        return self.getOrigin().getInnovationNum() * MAX_NODES * self.getTarget().getInnovationNum()
