import random
import time
import os
lista_nomes = []
lista_sorteados = []


print(30*"-","Bem vindo ao sistema de sorteios")
while True:
    nome = input("Digite um nome para ser sorteado: ").title()
    lista_nomes.append(nome)

    opcao = input("Deseja adicionar mais um nome? (s - sim) ou enter para parar! ").lower()
     
    if opcao != "s":
        break


while True:
    if not lista_nomes:
        print('A lista de nomes está vazia!')
        break
    else:
        nome_sorteado = random.choice(lista_nomes)
        lista_nomes.remove(nome_sorteado)
        lista_sorteados.append(nome_sorteado)
        


    for i in range(5,0,-1):
        time.sleep(1)
        print(f'Contagem regressiva...{i}')
        os.system('cls')

    print(f'O sorteado foi: {nome_sorteado}')

    sortear_novamente = input('Deseja sortear outro nome ? (s - sim | n - não)')

    if sortear_novamente == "n":
        print(lista_sorteados)
        break

print('Fim do programa')
