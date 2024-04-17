vetor = [7, 12, 0, -3, 5, 100]
procurado = int(input("Informe o elemento a ser procurado no vetor:"))


if procurado in vetor:
	print(f"O vetor {procurado} se encontra no vetor!")
else
	print(f" O valor {procurado} não se encontra no vetor!")

#ou

if procurado in not vetor:
	print(f" O valor {procurado} não se encontra no vetor!")
else
	print(f"O vetor {procurado} se encontra no vetor!")
