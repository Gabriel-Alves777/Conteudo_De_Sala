"""
    TIPOS DE DADOS
"""          
    
from tkinter import SE


str() 
int()
bool()
float()

nome = "Gabriel Aves Corrêa"
idade = 17
altura = 1.75
aluno = True

# variável com valor definido
print("Nome", nome)
print("Idade", idade)
print("Altura", altura)
print("Aluno", aluno)

# entrada de dados
input("Digite o seu nome: ")
input("DIgite a sua idade: ")
input("DIgite a sua altura ")

#NOTE - 
input

"""Desenvolva um sistema que receba do usuario seu nome, data de nascimento, peso e altura.
Formate a saida para aparecer na tela do usuario:
Olá {nome_informado}, seja bem-vindo ao sistema Python
Aqui estão as suas informações 
    Data Nascimento
    Altura
    Pes
    """

nome = input("Digite seu nome: ")
dataNa = input("Digite sua data de nascimento: ")
altura = input("Digite a sua altura: ")
peso = input("Digite o seu peso: ")

print("Olá", nome, " Bem-Vindo ao sistema Python")
print("Você nasceu no dia: ",dataNa)
print("A sua altura é: ", altura)
print("O seu peso é: ", peso)

print(type(nome))