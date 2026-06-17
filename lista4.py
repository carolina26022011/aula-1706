#descobrindo o tamanho da lista
nomes = ["wilson", "bianca", "ronaldo", "silmara", "juliano"]

print(len(nomes))

#saber se existe um elemento na lista
if "wilson" in nomes:
    print("está na lista")
else:
    print("não esta na lista")

#a posição de um elemento na lista
indice = nomes.index("bianca")
print(f"a bianca está no indíci {indice}")

#percorer a lista
for nome in nomes:
    print(nome)

#percorrer a lista com índice e valor
for name, nome in enumerate(nomes):
    print(name, nome)

#limpar toda lista
nomes.clear()
print(nomes)

nomes.append("wilson")
print(nomes)