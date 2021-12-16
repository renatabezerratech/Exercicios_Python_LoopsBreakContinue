#Criei uma função que vai pausar (pular) uma condição e continuar o programa;
#Para isso, no lugar de break, se usa continue;
#Foi usado o loop for com x no intervalo de 1 até 10;
#Na condição, se x for igual a 7, vai pular e continuar no próximo (x igual a 8);
#A verificação com print é feita dentro da função, mas fora do if (observe a indentação).


def loppContinue():
    for x in range (1,10):
        if x == 7:
            continue   #Passe para o próximo ítem do loop.
        print ("Valor de x é: ",x)

#Chama a função:
loppContinue()

