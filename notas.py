notas = input("Digite as notas na mesma linha separadas por um espaço em branco: ").split("  ")

print(notas) #texto

#O comando for realizada a conversão de texto para float, um a um
for i in range(len(notas)):
	notas[i] = float(notas[i])
print(notas) #float
media = sum(notas)/len(notas)
print(media)
