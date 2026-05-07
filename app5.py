'''
 Programa 01 - Aula04 - 28/04
 Prof Karython
 Turma 2º   
'''


import os
import random

print(30*"-", "Bem VIndo ao sistema de sorteios")

lista_nomes = []
    
    
lista_sorteados = []
sorteados = 0
while sorteados <5:
    sorteados +=1
    nome_sorteado = random.choice(lista_nomes)
    print(f'Sorteado: {nome_sorteado}')
    lista_sorteados.append(nome_sorteado)
    print(f'Lista atualizada (len{lista_nomes}')
    lista_nomes.remove(nome_sorteado)



print('Fim do programa')

