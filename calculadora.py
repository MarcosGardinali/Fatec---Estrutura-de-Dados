class calculadora:
    def __init__(self, x, y, n):
        self.a = x
        self.b = y
        self.nome = n

    def soma(self):
        return self.a + self.b
    
    def subtrai(self):
        return self.b - self.a
    
    def multiplica(self):
        return self.a*self.b
    
    def divide(self):
        return self.a/self.b

nome = input("Digite um nome: ")
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
y = calculadora(x=a, y=b, n=nome)

s = y.soma()

print("Nome: ", y.nome)
print("Soma", s)
print("Subtração", y.subtrai())
print("Multiplicação", y.multiplica())
print("Divisão", y.divide())