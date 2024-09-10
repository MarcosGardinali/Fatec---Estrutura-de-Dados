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
        self.Fim = None
        
    def Ins_Inicio(self, val):
        p = No(val)
        p.setProx(self.Inicio)
        
        if(self.Inicio == None):
            self.Fim = p
            
        self.Inicio = p
        
    def Ins_Fim(self, val):
        p = No(val)
        if(self.Inicio==None):
            self.Inicio = p
        else:
            self.Fim.setProx(p)
            
        self.Fim = p
        
    def Imprime(self):
        p = self.Inicio
        while p != None:
            print(p.getInfo(), "--> ", end='')
            p = p.getProx()
        print("None")
        
    def Rem_Inicio(self):
        if(self.Inicio.getProx() == None): #Só tem 1 nó
            self.Inicio = None
            self.Fim = None
        else:
            self.Inicio = self.Inicio.getProx()
            
    def Rem_Fim(self):
        if(self.Inicio.getProx() == None): #Só tem 1 nó
            self.Inicio = None
            self.Fim = None
        else:
            p = self.Inicio
            while p.getProx() != self.Fim:
                p = p.getProx()
            self.Fim = p
            self.Fim.setProx(None)
    
    def Consultar(self, val):
        p = self.Inicio
        while (p != None and p.getInfo() != val):
            p = p.getProx()

        return p
    
    def Trans_Fim(self, r):
        if(r == self.Inicio):
            self.Inicio = r.getProx()
        else:
            p = self.Inicio
            while(p.getProx() != r):
                p = p.getProx()
            
            p.setProx(r.getProx())
        
        r.setProx(None)
        self.Fim.setProx(r)
        self.Fim = r
            
    def Trans_Inicio(self, r):
        if(r == self.Fim):
            p = self.Inicio
            while (p.getProx() != self.Fim):
                p = p.getProx()
            
            p.setProx(None)
            self.Fim = p
        else:
            p = self.Inicio
            while(p.getProx() != r):
                p = p.getProx()
            
            p.setProx(r.getProx())
        
        self.Ins_Inicio(r.getInfo())
        
        
L = LSE()
while True:
    print("\n1 - Inserir no Início! ")
    print("2 - Inserir no Fim! ")
    print("3 - Imprimir a Lista! ")
    print("4 - Remover no Início! ")
    print("5 - Remover no Fim! ")
    print("6 - Consultar um No! ")
    print("7 - Transferir um No para o Fim! ")
    print("8 - Transferir um No para o Início! ")
    print("0 - Sair do Programa! ")
    
    op = int(input("\n Digite a opção: "))
    
    if(op == 0):
        break
    elif(op == 1):
        val = int(input("\n Digite o valor a inserir: "))
        L.Ins_Inicio(val)
    elif(op == 2):
        val = int(input("\n Digite o valor a inserir: "))
        L.Ins_Fim(val)
    elif(op == 3):
        if(L.Inicio == None):
            print("\n Lista Vazia!")
        else:
            print("\n Lista: ")
            L.Imprime()
    elif(op == 4):
        if(L.Inicio == None):
            print("\n Lista Vazia!")
        else:
            L.Rem_Inicio()
    elif(op == 5):
        if(L.Inicio == None):
            print("\n Lista Vazia!")
        else:
            L.Rem_Fim()
    elif(op == 6):
        val = int(input("\nDigite o valor a procurar: "))
        r = L.Consultar(val)
        if(r == None):
            print("\nValor não existe na lista!")
        else:
            print("\nValor encontrado:", r.getInfo())
    elif(op == 7):
        val = int(input("\nDigite o valor a transferir: "))
        r = L.Consultar(val)
        if(r == None):
            print("\nValor não existe na lista!")
        else:
            if(r == L.Fim):
                print("\nEste Nó já é o último!")
            else:
                L.Trans_Fim(r)
    elif(op == 8):
        val = int(input("\nDigite o valor a transferir: "))
        r = L.Consultar(val)
        if(r == None):
            print("\nValor não existe na lista!")
        else:
            if(r == L.Inicio):
                print("\nEste Nó já é o primeiro!")
            else:
                L.Trans_Inicio(r)
           