matriz_3x4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

print(matriz_3x4)

print("\nMatriz apresentada:\n")

for lin in range(3):
	for col in range(4):
		print(f"{matriz_3x4[lin][col]: 10d}", end="") #o comando end= informa para não mudar de linha e 
		# 10d - (10 posições, ou seja, espaços entre as colunas na tela = é a formatação do valor da matriz
		# o d= inteiro decimnal 
	print()
