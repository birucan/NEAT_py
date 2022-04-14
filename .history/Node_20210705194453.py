import numpy as np


from functools import total_ordering


@total_ordering
class Node:
    x=-1
    output =-1
    connections = []

    def __init__(self, nX):
        self.connections = []
        self.x = nX

    def calculate(self):
        s=0
        for a in self.connections:
            #print("a  "+str(a.getOrigin()))
            if(a.isEnabled()):
                s += a.getWeight()*a.getTarget().getOutput()
        self.output=self.activationFunction(s)

    def activationFunction(self, foo):
        return 1/(1+ np.exp(-foo))


    ############

    def getX(self):
        return self.x

    def setX(self, nX):
        self.x= nX

    def setOutput(self, nOutput):
        self.output = nOutput

    def getOutput(self):
        return self.output

    def getConnections(self):
        return self.connections

    def setConnections(self, nConnections):
        self.connections = nConnections

    #I have no plans to learn how to properly implement comparables in python anytime soon
    def compareTo(self, obj):
        if(this.x > obj.x): return -1
        if(this.x < obj.x): return 1
        else: return 0

    #NVM im gonna try
    def __eq__(self, obj):
        return (self.x==obj.x)


    def __lt__(self, obj):
        return (self.x< obj.x)


    def __gt__(self, obj):
        return (self.x > obj.x)
