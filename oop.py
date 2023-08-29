import random

class Player:
    def __init__(self, sum = 500, bet = 0, number = 0, random_num = 0, validation = True):
        self.sum = sum
        self.bet = bet
        self.number = number
        self.random_num = random_num
        self.validation = validation

    def greeting(self):
        print('Вы в игре. На счету 500 монет.')
    
    def make_bet(self):
        print('Введите ставку.')
        bet = int(input())
        self.bet = bet
    
    def choose_number(self):
        print('Ваш номер?')
        number = int(input())
        self.number = number

    def randomizing(self):
        random_num = random.randint(1, 6)
        self.random_num = random_num

    def is_win(self):
        print(f'Выпало - {self.random_num}')
        if self.random_num == self.number:
            self.sum = self.sum + self.bet*2 
            print(f'Вы победили. На счету {self.sum}')   
        else:
            self.sum = self.sum - self.bet
            print(f'Вы проиграли. На счету {self.sum}')
        print('***********************************************************')

    def make_validation(self):
        if self.bet > self.sum:
            print(f'Недостаточно монет, введите меньше или равную = {self.sum}')
            self.validation = False
        else:
            self.validation = True
            

Gamer = Player()

Gamer.greeting()
while Gamer.sum != 0:
    Gamer.make_bet()
    Gamer.make_validation()
    if Gamer.validation == True:
        Gamer.choose_number()
        Gamer.randomizing()
        Gamer.is_win()
    
    

    



