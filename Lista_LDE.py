class No:
    def __init__(self, val):
        self.esq = None
        self.info = val
        self.dir = None
        
    def getEsq(self):
        return self.esq
    
    def getDir(self):
        return self.dir
    
    def getInfo(self):
        return self.info
    
    def setEsq(self, anterior):
        self.esq = anterior
        
    def setDir(self, proximo):
        self.dir = proximo
        
    def setInfo(self, val):
        self.info = val
            
class LDE:
    def __init__(self):
        self.Inicio = None
        self.Fim = None
        
    def Ins_Inicio(self, val):
        p = No(val)
        if(self.Fim == None):
            self.Fim = p
        else:
            p.setDir(self.Inicio)
            self.Inicio.setEsq(p)
            
        self.Inicio = p
        
    def Ins_Fim(self, val):
        p = No(val)
        if(self.Inicio == None):
            self.Inicio = p
        else:
            p.setEsq(self.Fim)
            self.Fim.setDir(p)
            
        self.Fim = p
        
    def Imprime(self):
        p = self.Inicio
        print("None", end='')
        while(p != None):
            print(" <--", p.getInfo(), "-->", end='')
            p = p.getDir()
            
        print(" None")
        
    def Rem_Inicio(self):
        if(self.Inicio == self.Fim):
            self.Inicio = None
            self.Fim = None
        else:
            self.Inicio = self.Inicio.getDir()
            self.Inicio.setEsq(None)
        
    def Rem_Fim(self):
        if(self.Inicio == self.Fim):
            self.Inicio = None
            self.Fim = None
        else:    
            self.Fim = self.Fim.getEsq()
            self.Fim.setDir(None)
    
        
L = LDE()

while True:
    print("\n1 - Inserir no Início da Lista! ")
    print("2 - Inserir no Fim da Lista! ")
    print("3 - Imprimir a Lista! ")
    print("4 - Remover no Inicio! ")
    print("5 - Remover no Fim! ")
    print("0 - Sair do Programa! ")
    
    op = int(input("\n Digite a opção: "))
    
    if(op == 0):
        break
    elif(op == 1):
        val = int(input("\nDigite o valor a inserir: "))
        L.Ins_Inicio(val)
    elif(op == 2):
        val = int(input("\nDigite o valor a inserir: "))
        L.Ins_Fim(val)    
    elif(op == 3):
        if(L.Inicio == None):
            print("\nLista Vazia!")
        else:
            print("\nLista: ")
            L.Imprime()
    elif(op == 4):
        if(L.Inicio == None):
            print("\nLista Vazia!")
        else:
            L.Rem_Inicio()
    elif(op == 5):
        if(L.Inicio == None):
            print("\nLista Vazia!")
        else:
            L.Rem_Fim()
    
   