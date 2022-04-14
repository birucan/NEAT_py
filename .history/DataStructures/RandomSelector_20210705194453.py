import random

class RandomSelector:

    scores= []
    objects= []
    totalScore = 0;


    def __init__(self):
        self.scores=[]
        self.objects=[]

    def add(self, element, score):
        self.scores.append(score)
        self.objects.append(element)
        self.totalScore += score


    def getRandom(self):
        v= random.random()*self.totalScore

        c= 0
        for a in range(0, len(self.objects)):
            c += self.scores[a]
            if(c>v):
                return self.objects[a]

    def clear(self):
        self.scores=[]
        self.objects=[]
        self.totalScore=0


def tester():
    test = RandomSelector()

    test.add('test', 200000000)
    test.add('test2', 2000)
    test.add('test3', 5000)

    print(test.getRandom())

#tester()
