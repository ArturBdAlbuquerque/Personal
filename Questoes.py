"1)"
indice = 13
soma = 0
k = 0
while(k < indice):
    k = k + 1
    soma += k
print(soma)

"2)"
desejado = int(input("Informe o número desejado: "))
primeiro = 0
segundo = 1
while segundo < desejado:
    proximo = primeiro + segundo
    primeiro = segundo
    segundo = proximo
if segundo == desejado or primeiro == desejado:
    print("Pertence")
else:
    print("Não pertence")

"3a)"
sequencia = [1,3]
while sequencia[-1]  <= 7:
    proximo = sequencia[-1] + 2
    sequencia.append(proximo)
print(sequencia)

"3b)"
sequencia = [2]
while sequencia[-1]  <= 64:
    proximo = sequencia[-1] * 2
    sequencia.append(proximo)
print(sequencia)

"3c)"
sequencia = [0]
complemento = 1
while sequencia[-1]  <= 36:
    proximo = sequencia[-1] + complemento
    sequencia.append(proximo)
    complemento += 2
print(sequencia)

"3d)"
sequencia = [4]
complemento = 12
while sequencia[-1]  <= 64:
    proximo = sequencia[-1] + complemento
    sequencia.append(proximo)
    complemento += 8
print(sequencia)

"3e)"
sequencia = [1,1]
while sequencia[-1] <= 8:
    proximo = sequencia[-1] + sequencia[-2]
    sequencia.append(proximo)
print(sequencia)

"3f) 200"

"4) Ambos, pois quando eles se cruzarem, significa que os dois estarão no mesmo ponto da rodovia, e a distância desse ponto até Ribeirão Preto é 61 Km."
"Esse valor se dá devido ao tempo de 33 minutos que leva para os dois veículos se cruzarem, que foi encontrado a partir de método de tentativa e erro com regra de três"
"com diferentes tempos. Assim, aos 33 minutos, o carro terá percorrido 61 km enquanto o caminhão terá percorrido 39 km"

"5)"
texto = "abacate"
auxiliar = ""
i = 1
while i <= len(texto):
    auxiliar += texto[-i]
    i += 1
texto = auxiliar
print(texto)