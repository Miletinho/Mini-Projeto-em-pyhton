import json

def primeira_pista():
    f=open('pistas.json',)
    data=json.load(f)
    print(data['Aeroporto'])
    f.close()

def jogar():
    intro = open("introdução.txt", "r")
    print(intro.read())
    print('''
Sera que voce consegue resolver esse misterio? 
        
Caso deseje jogar escreva "sim", caso contrario escreva "nao".''')
    x = input()
    if x == 'sim':
        print("Que comece o jogo!")
        primeira_pista()
    else:
        print("OK, até uma próxima ")
jogar()
