#Criei uma função para usar o comando break, que interrompe o loop;
#A função não tem parâmetros, usa loop for em intervalo (comando range);
#O comando break é usado na condição especificada em if;
#A verificação com print é feita dentro da função, mas fora do if (observe a indentação).

def loppBreak():
    for x in range (1,10):
        if x == 8:
            break    #Interrompa a função nesse ítem.
        print ("Valor de x é: ",x)

#Chama a função:
loppBreak()



        