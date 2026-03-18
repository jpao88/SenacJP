

frutas = ["maça", "banana", "uva"]
numeros = [1,2,3,4]

print("Lista original 'frutas':", frutas)

#Acessando elementos
print("Primeira fruta:", frutas[0])
print("Última fruta:", frutas[-1])

#Alterando elementos
frutas[1] = "banana-nanica"
print("Após alterar:", frutas)

#Adicionando elementos
frutas.append("morango")        #adiciona no final
frutas.insert(1,"pera")         #adiciona na posição 1
print("Após adicionar:", frutas)

#Removendo elementos
frutas.remove("uva")        #remove pelo valor
ultima = frutas.pop()       #remove e retorna o último
print("Após remover 'uva' e pop():", frutas, "| Última removida:", ultima)

#Outras operações úteis
print("Lista original 'numeros':", numeros)
print("Soma dos números:", sum(numeros))
print("Maior número:", max(numeros))
print("Menor número:", min(numeros))
numeros.reverse()
print("Reversa:", numeros)
numeros.sort()
print("Ordenada crescente:", numeros)
numeros.sort(reverse=True)
print("Ordenada decrescente:", numeros)

#Iterar sobre lista
for fruta in frutas:
    print("Fruta:", fruta)

#List comprehension (exemplo simples)
quadrados = [n * n for n in [1, 2, 3, 4, 5]]
print("Quadrados:", quadrados)

#TUPLAS

#Criando tuplas
coordenadas = (10, 20)
dias = ("segunda", "terça", "quarta", "quinta", "sexta")

#Acessando elementos
print("X:", coordenadas[0], "| Y:", coordenadas[1])

#Slicing (fatiamento) em tuplas
print("Primeiros 3 dias:", dias [:3])

#Tamanho
print("Tamanho da tupla 'dias':", len(dias))

#Verificar se um elemento está na tupla
print("Tem 'segunda'?", "segunda" in dias)

#Contagem e índice em tuplas
print("Contagem de 'terça':", dias.count("terça"))
print("Índice de 'quarta':", dias.index("quarta"))











