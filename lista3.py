#excluir pelo valor
pecas = ["retrovisor", "volante", "buzina", "pedais", "pastilha de freio", "bomba de água"]
for peca in pecas:
    print(pecas)
pecas.remove("buzin")
print(pecas)

pecas.pop(0)
print(pecas)

del pecas[1]
print(pecas)
