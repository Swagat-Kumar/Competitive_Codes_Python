class stack:
    def __init__(self):
        self.s = []
        self.aux = []
        self.minEle = None

    def push(self, x):
        # CODE HERE
        if self.minEle == None:
            self.minEle = x
            self.s.append(x)
            self.aux.append(x)
        elif self.minEle > x:
            self.aux.append(2*x-self.minEle)
            self.minEle = x
            self.s.append(x)
        else:
            self.s.append(x)
            self.aux.append(x)

    def pop(self):
        # CODE HERE
        if len(self.s) == 0:
            return -1
        temp = self.aux.pop()
        if temp <= self.minEle:
            if len(self.aux) == 0:
                self.minEle = None
            else:
                self.minEle = 2*self.minEle-temp
        return self.s.pop()

    def getMin(self):
        # CODE HERE
        if len(self.s) == 0:
            return -1
        return self.minEle
