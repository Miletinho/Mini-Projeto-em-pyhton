import json
import random

random.seed(a=None, version=2)
qtd_lugares = 18
f=open('pistas.json')
j=open('lugares.json')
m=open('mapa.json')
pistas=json.load(f)
lugares =json.load(j)
mapa=json.load(m)

pos = {}
m=1
for i in lugares: 
    pos[i] = m
    m=m+1

def pistas_default(lugar):
    l = lugares[lugar]
    if mapa[l][-1]!=0:
        print(f''' 
Voce ja passou por aqui!!!!, mas como estou de bom humor sua dica é:

\033[92m {pistas[l]}\033[m

Para onde voce quer ir agora?
        ''')
    else: 
        mapa[l][-1]=1
        print(
            f'''
Voce está em {l} ! Sua dica é:

\033[92m {pistas[l]}\033[m

Para onde voce quer ir agora?
            ''')
    for i in range(0, len(mapa[l])-1):
        print(f'''({pos[mapa[l][i]]})\033[93m {mapa[l][i]} \033[m ''')
    x=int(input('Opção:'))
    pistas_default(x-1)
    

def primeira_pista():
    r = random.randrange(qtd_lugares)
    pistas_default(r)


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
