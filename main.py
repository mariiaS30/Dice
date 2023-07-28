import random

print('Вы в игре. На счету 500 монет.')
sum = 500


while sum != 0:
    print('Введите ставку.')
    bet = int(input())
    if bet > sum:
        print(f'Недостаточно монет, введите меньше или равную = {sum}')
    else:
        print('Ваш номер?')
        number = int(input())
        random_num = random.randint(1, 6)
        print(f'Выпало - {random_num}')
        if random_num == number:
            sum = sum + bet*2
            print(f'Вы победили. На счету {sum}')
        else:
            sum = sum - bet
            print(f'Вы проиграли. На счету {sum}')
        print('***********************************************************')
    



