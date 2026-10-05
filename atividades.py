#lista de alunos

alunos = ["Mirela", "João"]
alunos.append("Daniela")
print("Lista de alunos", alunos)

alunos_para_remover = input("Deseja remover um nome?")
if alunos_para_remover in alunos:
    alunos.remove(alunos_para_remover)
    print("Aluno removido.")
else:
    print("O aluno não está na lista.")

print("Lista de alunos", alunos)


#Lista de compras

compras = []
compras1 = 'pacote de arroz'
compras.append(compras1)
compras2 ='picanha'
compras.append(compras2)
compras3 = 'Farofa'
compras.append(compras3)

#Ordenando números na forma crescente

numeros = [10, 3, 9, 4, 7]
lista_ordenada = sorted(numeros)

print("Sorteio de números", numeros)

print("Lista de compras", compras)
