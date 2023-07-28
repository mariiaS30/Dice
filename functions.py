import random

def play():    
    print('Вы в игре. На счету 500 монет.')
    sum = 500

def make_bet():
    print('Введите ставку.')
    bet = int(input())
    return bet

def choose_number():
    print('Ваш номер?')
    number = int(input())
    return number

def is_win(number):
    random_num = random.randint(1, 6)
    print(f'Выпало - {random_num}')
    if random_num == number:
        sum = sum + bet*2
        print(f'Вы победили. На счету {sum}')
    else:
        sum = sum - bet
        print(f'Вы проиграли. На счету {sum}')
     print('***********************************************************')


#разбить функцию из вин(рандом и остальное), исправить строчку 17