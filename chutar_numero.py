import random

def jogar():
    print('olá, tente a sorte digite um número:')
    x= random.randint(1,10)
    y=int(input())
    while(y!=x): 
        print('errou tente novametne')
        y=int(input())
    print('parabéns voce acertou:')
    print('Quer tentar novamente ?:1 para sim e 0 para não')
    z=input()
    if z==0: 
        jogar()
    else: 
        print('até uma póxima!')
    
    
jogar()