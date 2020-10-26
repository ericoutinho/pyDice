import random

class Dice:
    def __init__(self, minimo=1, maximo=6):
        self.minimo = minimo
        self.maximo = maximo
        self.message = "🎲 Deseja rolar o dado? (s/n) "

    def lancar(self):
        question = input(self.message).lower()
        try:
            if question == 's' or question == 'sim':
                self.roll()
            elif question == 'n' or question == 'não':
                print('😥 Ok. Quem sabe outra hora...')
            else:
                print('😣 Favor informar sim ou não')
                self.lancar()
        except:
            print('😱 Ocorreu um erro!')
    
    def roll(self):
        print('😎 O valor do dado é:', random.randint(self.minimo, self.maximo))
        self.lancar()

myDice = Dice()
myDice.lancar()