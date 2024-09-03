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
    
    def Consultar(self, val):
        p = self.Inicio
        while (p != None and p.getInfo() != val):
            p = p.getProx()

        return p
    
    def Rem_Meio(self, r):
        p = self.Inicio
        while (p.getProx() != r):
            p = p.getProx()

        p.setProx(r.getProx())
        
    def Ins_Depois(self, r, val):
        p = No(val)
        p.setProx(r.getProx())
        r.setProx(p)
        
    def Ins_Antes(self, r, val):
        p = No(val)
        q = self.Inicio
        while(q.getProx() != r):
            q = q.getProx()
        
        p.setProx(q.getProx())
        q.setProx(p)
        
    def Ins_Ordenado(self, val):
        q = self.Inicio
        if(val < q.getInfo()):
            self.Ins_Inicio(val)
        else:
            while(q != None and q.getInfo() < val):
                q = q.getProx()
                
            if(q == None):
                self.Ins_Fim(val)
            else:
                self.Ins_Antes(q, val)
            
        

    def Imprime(self):
        p = self.Inicio
        while p != None:
            print(p.getInfo(), "--> ", end ='')
            p = p.getProx()

        print("None")

L = LSE()

while True:
    print("\n1 - Para inserir um valor ao início!")
    print("2 - Para imprimir a lista!")
    print("3 - Inserir um valor ao final!")
    print("4 - Apagar o valor no início!")
    print("5 - Apagar o valor no fim!")
    print("6 - Consultar nó!")
    print("7 - Remover um nó!")
    print("8 - Inserir depois de um nó!")
    print("9 - Inserir antes de um nó!")
    print("10 - Inserir de forma ordenada!")
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
    if(op == 6):
        val = int(input("Digite o valor a procurar: "))
        r = L.Consultar(val)
        if(r == None):
            print("\nValor não existe na lista!")
        else:
            print("\nValor encontrado:", r.getInfo())
    if(op == 7):
        val = int(input("Digite o valor a remover: "))
        r = L.Consultar(val)
        if(r == None):
            print("\nValor não existe na lista!")
        else:
            if(r == L.Inicio):
                L.Rem_Inicio()
            else:
                if(r.getProx() == None):
                    L.Rem_Fim()
                else:
                    L.Rem_Meio(r)
            
            print("\nValor Removido: ", r.getInfo())
            print("Lista atualizada:")
            L.Imprime()
    if(op == 8):
        val = int(input("Digite o valor a procurar: "))
        r = L.Consultar(val)
        if(r == None):
            print("\n Valor Não existe na lista!")
        else:
            val = int(input("Digite o valor a inserir: "))
            if(r.getProx == None):
                L.Ins_Fim(val)
            else:
                L.Ins_Depois(r, val)
    if(op == 9):
        val = int(input("Digite o valor a procurar: "))
        r = L.Consultar(val)
        if(r == None):
            print("\n Valor Não existe na lista!")
        else:
            val = int(input("Digite o valor a inserir: "))     
            if(r == L.Inicio):
                L.Ins_Inicio(val)
            else:
                L.Ins_Antes(r, val)
                
    if(op == 10):
        val = int(input("Insira o valor a ser inserido de forma ordenada: "))
        if(L.Inicio == None):
            L.Ins_Inicio(val)
        else:
            L.Ins_Ordenado(val)