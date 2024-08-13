class no:
    def __init__(self, val):
        self.info = val
        self.prox = None


    def getInfo(self):
        return self.info
    
    def getProx(self):
        return self.prox
    
    def setInfo(self, val):
        self.info = val

    def setProx(self, proximo):
        self.prox = proximo