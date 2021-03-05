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
        self.objects.append(object)
        self.totalScore += score


    def getRandom(self):
        v= random.random()*self.totalScore

        c= 0
        for a in range(0, len(self.scores)):
            c += self.scores[a]
            if(c>v):
                print(a)
                return self.objects[a]

    def clear(self):
        self.scores=[]
        self.objects=[]
        self.totalScore=0


def tester():
    test = RandomSelector()

    test.add('test', 2000)
    test.add('test2', 2000)
    test.add('test3', 500)

    print(test.getRandom())

#tester()
