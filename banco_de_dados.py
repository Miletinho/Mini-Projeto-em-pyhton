from random import choice 

respostas=['Sim', 'Não', 'Sim!', 'Não!', 'Acho que sim...', 'Acho que não...', 'Óbvio que sim', 'Óbvio que não', 'Claro que sim', 'Claro que não', 'Talvez...', 'Melhor não...', 'Com certeza!', 'Não sei...', 'Sei lá', 'Não posso responder isso', 'Você que sabe', 'Se você quer...', 'A decisão é sua!']

while True:
    pergunta = input('Qual a sua pergunta ? \n')

    if pergunta.isalpha() !=True and not '?' in pergunta:
        print("Ei, é pra fazer uma pergunta!!!!!!!!!!!!!!")
        continue
    else:
        print(choice(respostas))