'''abstração: só pega oq é necessário no momento
encapsulamento: proteção
herança: capacidade de uma classe herdar métodos (ações) e atributos (características) de outra classe
polimorfismo: recebe e reescreve para adaptar
classe abstrata: foi criada para servir de modelo para outras classes herdarem características '''

class Pessoa():
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.andando = False
        self.dormindo = False

    def comer(self):
        if self.comendo == False:
            if self.andando == False:
                if self.dormindo == False:
                    print(f"{self.nome} foi comer.")
                    self.comendo = True
                else:
                    print(f"{self.nome} não pode comer pois está dormindo.")
            else:
                print(f"{self.nome} não pode comer pois está andando.")
        else:
            print(f"{self.nome} já está comendo.")

    def andar(self):
        if self.andando == False:
            if self.comendo == False:
                if self.dormindo == False:
                    print(f"{self.nome} começou a andar.")
                    self.andando = True
                else:
                    print(f"{self.nome} não pode andar pois está dormindo.")
            else:
                print(f"{self.nome} não pode andar pois está comendo.")
        else:
            print(f"{self.nome} já está andando.")



class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
      print(f"O {self.nome} foi comer...")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def miar(self):
        print(f"O {self.nome} foi miando...")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def comer(self):
        print(f"O cachorro {self.nome} foi comer...")

    def latir(self):
        print(f"O {self.nome} foi latindo...")

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def chiar(self):
        print(f"O {self.nome} foi chiando...")

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def mugir(self):
        print(f"A {self.nome} foi mugindo...")



class Atleta():
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso
        self.aposentado = False
        self.aquecido = False

    def aposentar(self):
        if self.aposentado == False:
            print(f"{self.nome} foi aposentado.")
            self.aposentado = True
        else:
            print(f"{self.nome} não pode aposentar porque já está na rede!")

    def aquecer(self):
        if self.aquecido == False:
            if self.aposentado == False:
                print(f"{self.nome} está aquecido.")
                self.aquecido = True
            else:
                print(f"{self.nome} não pode aquecer pois está aposentado.")
        else:
            print(f"{self.nome} não pode aquecer pois já está aquecendo.")

class Corredor(Atleta):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)

    def correr(self):
        if self.aquecido == True:
            print(f"{self.nome} foi correr.")
        else:
            print(f"Não pode correr pois não aqueceu.")

class Nadador(Atleta):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)

    def nadar(self):
        if self.aquecido == True:
            print(f"{self.nome} foi nadar.")
        else:
            print(f"Não pode nadar pois não aqueceu.")

class Ciclista(Atleta):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)

    def nadar(self):
        if self.aquecido == True:
            print(f"{self.nome} foi pedalar.")
        else:
            print(f"Não pode pedalar pois não aqueceu.")

class TriAtleta(Corredor, Nadador, Ciclista):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)

def cadastrar(texto):
    with open("registro.txt", "a") as arq:
        arq.write(f"{texto}\n")
def mostrar():
    with open("registro.txt", "r") as arq2:
        leitura = arq2.read()
        print(leitura)
def pesquisar(texto):
    try:
        cont = 0
        with open("registro.txt", "r") as arquivo:
            for x in arquivo:
                if texto in x:
                    cont+=1
                else:
                    print("Texto não encontrado")
        print(cont)
    except FileNotFoundError:
        with open("registro.txt", "a"):
            pass
