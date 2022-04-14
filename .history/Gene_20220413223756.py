
class Gene:

    innovationNum=-1

    def __init__(self, pInnovationNum):
        self.innovationNum=pInnovationNum

    def getInnovationNum(self):
        return self.innovationNum

    def setInnovationNum(self, newIn):
        self.innovationNum= newIn
