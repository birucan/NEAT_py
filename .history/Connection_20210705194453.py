from Gene import *
from Node import *
from Constants import *

class Connection(Node):

    origin = Node(-1)
    target = Node(-1)

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
        self.weight = nWeight

    def isEnabled(self):
        return self.enabled

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def toggle(self):
        if(self.isEnabled()):
            self.disable()
        else:
            self.enable()

    def setEnabled(self, state):
        if(type(state) == bool):
            self.enabled = state
