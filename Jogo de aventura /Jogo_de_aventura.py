import json
import os
from os import register_at_fork
import random
import time


random.seed(a=None, version=2)
qtd_lugares = 18
f=open('pistas.json')
pistas=json.load(f)
j=open('lugares.json')
lugares =json.load(j)
m=open('mapa.json')
mapa=json.load(m)
k=open('possibilidades.json')
possibilidades=json.load(k)
s=open('solucao.json')
solucao=json.load(s)
e=open('explicacao.txt',"r")


perguntas = ["Quem é o Assassino?", "Qual foi o Motivo?", "Qual foi a Arma?", "Quem é o Homem Desconhecido?"]
possi = ["Assassino", "Motivo", "Arma", "Homem Desconhecido"]

pos = {}
n=1
for i in lugares: 
    pos[i] = n
    n=n+1

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def ganhou():
    print('Parabéns!!!! Você resolveu o mistério com louvor!')
    print(e.read())
    input("Você poderá jogar novamente! Estamos preparando tudo...")
    time.sleep(5)
    jogar()
    

def dar_palpite(index):
    clear()
    print(perguntas[index], '\n')
    n=1
    nome =possi[index]
    for i in possibilidades[nome]:
        print(f'''({n}) {i}''')
        n=n+1
    x=int(input())
    if possibilidades[nome][x-1]!=solucao[nome]:
        print("Infelizmente você errou, mas pode continuar tentando!")
        return False
    else: 
        if index == len(solucao)-1 : 
            return ganhou()
        else:
            return dar_palpite(index+1)

def pistas_default(lugar):
    clear()
    l = lugares[lugar]
    if mapa[l][-1]!=0:
        print(f''' 
Voce já passou por aqui!!!! Voce está em {l} ! Sua dica é:

\033[92m {pistas[l]}\033[m

O que você quer fazer agora?
        ''')
    else: 
        mapa[l][-1]=1
        print(
            f'''
Voce está em {l} ! Sua dica é:

\033[92m {pistas[l]}\033[m

O que você quer fazer agora?
            ''')
    print('(0)\033[93m Dar um Palpite \033[m')
    for i in range(0, len(mapa[l])-1):
        print(f'''({pos[mapa[l][i]]})\033[93m Ir para {mapa[l][i]} \033[m ''')
    print('(20)\033[93m Reler a introdução do caso \033[m \n')
    time.sleep(1)
    x=int(input('Opção: '))
    if x==0:
        d = dar_palpite(0)
        if d is False:
            time.sleep(2)
            pistas_default(lugar)
    elif x==20:
        intro=open("introdução.txt", "r")
        print(intro.read())
        x=input("Digite enter para continuar!")
        pistas_default(lugar)
    else:
        pistas_default(x-1)
    

def primeira_pista():
    r = random.randrange(qtd_lugares)
    pistas_default(r)


def jogar():
    clear()
    intro=open("introdução.txt", "r")
    print(intro.read())
    time.sleep(1)
    print('''
Sera que voce consegue resolver esse misterio? 
        
Caso deseje jogar escreva "sim", caso contrario escreva "nao".''')
    x = input()
    if x.lower() == 'sim':
        print("Que comece o jogo!")
        time.sleep(1)
        primeira_pista()
    else:
        print("OK, até uma próxima ")
jogar()
