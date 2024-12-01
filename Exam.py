import random
score = 0
i = 1
while i == 1:
    x = random.randint(2, 2)
    y = random.randint(1, 10)
    res = x * y
    print(x, ' x ', y, ' = ')
    ires=int(input())
    if ires == res:
        score += 1
        i = 1
        print('Верно! У тебя уже ', score, ' очков!')
    elif ires == 0:
        print('Устали, милорд? Отдохните! Вы набрали ', score, ' очков')
        i = 0
    else:
        i = 0
        print('Нет, ', res, 'Game Over, чувак! Ты набрал ', score,' очков!')
