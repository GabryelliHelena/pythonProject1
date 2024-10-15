'''abstração: só pega oq é necessário no momento
encapsulamento: proteção
herança: capacidade de uma classe herdar métodos (ações) e atributos (características) de outra classe
polimorfismo: recebe e reescreve para adaptar'''

'''class pessoa():
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
                print()'''