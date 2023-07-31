import random

def play():    
    print('Вы в игре. На счету 500 монет.')
    sum = 500
    while sum != 0:
        bet = make_bet()
        if validation(bet, sum):
            number = choose_number()
            random_num = randomizing()
            sum = is_win(number, random_num, sum, bet)

def make_bet():
    print('Введите ставку.')
    bet = int(input())
    return bet

def validation(bet, sum):
    if bet > sum:
        print(f'Недостаточно монет, введите меньше или равную = {sum}')
        return False
    return True

def choose_number():
    print('Ваш номер?')
    number = int(input())
    return number

def randomizing():
    random_num = random.randint(1, 6)
    return random_num

def is_win(number, random_num, sum, bet):
    print(f'Выпало - {random_num}')
    if random_num == number:
        sum = winning(sum, bet)    
    else:
        sum = losing(sum, bet)
    print('***********************************************************')
    return sum

def winning(sum, bet):
    sum = sum + bet*2
    print(f'Вы победили. На счету {sum}')
    return sum

def losing(sum, bet):
    sum = sum - bet
    print(f'Вы проиграли. На счету {sum}')
    return sum

play()


#разбить функцию из вин(рандом и остальное), исправить строчку 17