import random


def dado(number):

    fvalue = 0
    for qts in range(0, number):
        value = random.randint(1, 6)
        fvalue = fvalue + value
    return fvalue


def jogar():
    global y
    while 1 :
        y = 0
        try:
            x = int(input('Quantos dados deseja jogar? '))
        except:
            x = 0
        if x == 0:
            break
        y = dado(x)
        print('A soma foi de >>> %d' % (y))

jogar()
