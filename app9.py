import random
import time
import os

lista_nomes = []
lista_sorteados = []

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

print("-" * 30, "Bem vindo ao sistema de sorteios")
while True:
    nome = input("Digite um nome: ").title()
    if nome:
        lista_nomes.append(nome)

    opcao = input("Deseja adicionar mais um? (s/n): ").lower()
    if opcao != "s":
        break

while True:
    if not lista_nomes:
        print('A lista de nomes acabou!')
        break # Aqui deve ser break, não breakpoint
    
    nome_sorteado = random.choice(lista_nomes)
    
    # Efeito da contagem
    for i in range(3, 0, -1):
        limpar() # Chama a função de limpar
        print(f'Sorteando em... {i}')
        time.sleep(1)

    limpar()
    print(f'O sorteado foi: {nome_sorteado}')
    
    lista_nomes.remove(nome_sorteado)
    lista_sorteados.append(nome_sorteado)

    if not lista_nomes:
        print("Todos os nomes já foram sorteados!")
        break

    res = input('Deseja sortear outro? (s/n): ').lower()
    if res == "n":
        break

print(f'\nLista de sorteados final: {lista_sorteados}')
print('Fim do programa')