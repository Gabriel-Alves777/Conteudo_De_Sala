# NOTE: Boletim Escolar

# importa uma lib
from code import InteractiveInterpreter
import os

os.system("cls")

nome = input("Digite o nome do aluno: ")
turma = input("Digite o nome da turma: ")
nota1 = input("Digite a primeira nota do aluno: ")
nota2 = input("Digite a segunda nota do aluno:" )
nota3 = input("Digite a terceira nota do aluno: ")
nota4 = input("Digite a quarta nota do aluno: ")
nota5 = input("Digite a quinta nota do aluno: ")

nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
nota4 = float(nota4)
nota5 = float(nota5)
media = (nota1 + nota2 + nota3 + nota4 + nota5)/5

print(f'A media do aluno {nome} da turma {turma} é {media:.2f}')

