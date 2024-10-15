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
                    print(f"{self.nome} foi andar.")
                    self.andando = True
                else:
                    print(f"{self.nome} não pode andar pois está dormindo.")
            else:
                print()



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