import random
resutado=0
adversario=0

a=input()
baralho=[2,3,4,5,6,7,8,9,10,10,10,10,11]
escolha=random.choice(baralho)
bot=random.choice(baralho)

while a!='2':
    print('''selecione
          [1] para comprar
          [2] para parar o jogo
          ''')
    a=input()
    if a=='2':
        break
    escolha=random.choice(baralho)
    bot=random.choice(baralho)
    resutado=resutado+escolha
    adversario=adversario+bot
    print('_'*40)
    print('atualmente vc possui as cartas {} que somadas dão {}'.format(escolha,resutado))
    print('🤖')
    print('atualmente o BOT possui as cartas {} que somadas dão {}'.format(bot,adversario))
    print('_'*40)
    if adversario >=17:
        break

    
if adversario<resutado:
     bot=random.choice(baralho)
     adversario=adversario+bot
     print('atualmente vc possui as cartas {} que somadas dão {}'.format(escolha,resutado))
     print('🤖')
     print('atualmente o BOT possui as cartas {} que somadas dão {}'.format(bot,adversario))


while a!='2':
    print('''selecione
          [1] para comprar
          [2] para parar o jogo
          ''')
    a=input()
    if a=='2':
        break
    escolha=random.choice(baralho)
    resutado=resutado+escolha
    print('_'*40)
    print('atualmente vc possui as cartas {} que somadas dão {}'.format(escolha,resutado))
    print('🤖')
    print('atualmente o BOT possui as cartas {} que somadas dão {}'.format(bot,adversario))
    print('_'*40)


if adversario==resutado:
    print('empate')
elif resutado>adversario and resutado<22:
    print('vitoria')
elif adversario>21:
    print('vitoria')