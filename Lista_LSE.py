class No:
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

class LSE:
    def __init__(self):
        self.Inicio = None

    def Ins_Inicio(self, val):
        p = No(val)
        p.setProx(self.Inicio)
        self.Inicio = p

    def Ins_Fim(self, val):
        p = No(val)
        if(self.Inicio == None):
            self.Inicio = p
        else:
            q = self.Inicio
            while q.getProx() != None:
                q = q.getProx()
                
            q.setProx(p)

    def Rem_Inicio(self):
        self.Inicio = self.Inicio.getProx()

    def Rem_Fim(self):
        p = self.Inicio

        if(p.getProx() == None):
            self.Inicio = None
        else:    
            while p.getProx() != None:
                q = p
                p = p.getProx()
        
            q.setProx(None)

    def Imprime(self):
        p = self.Inicio
        while p != None:
            print(p.getInfo(), "--> ", end ='')
            p = p.getProx()

        print("None")

L = LSE()

while True:
    print("1 - Para inserir um valor ao início!")
    print("2 - Para imprimir a lista!")
    print("3 - Inserir um valor ao final!")
    print("4 - Apagar o valor no início!")
    print("5 - Apagar o valor no fim!")
    print("0 - Para sair!")

    op = int(input("\nDigite a opção: \n"))

    if(op == 0):
        break
    if(op == 1):
        val = int(input("\nInsira o valor que deseja inserir: "))
        L.Ins_Inicio(val)
    if(op == 2):
        if(L.Inicio == None):
            print("\nLista Vazia!\n")
        else:
            L.Imprime()
    if(op == 3):
        val = int(input("\nInsira o valor que deseja inserir: "))
        L.Ins_Fim(val)
    if(op == 4):
        L.Rem_Inicio()
    if(op == 5):
        L.Rem_Fim()