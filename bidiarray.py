array = [
    ["joão", "pedro", "marcia", "alvaro"],
    [43, 22, 31, 50],
    ["casa", "apartamento", "apartamento", "casa"]
]

i = 0

for i in range(len(array)):
    j = 0
    for j in range(len(array)):
        print(f"Nome: {array[i][j]}|\n Idade: {array[i+1][j]}|\n Domicilio: {array[i+2][j]}")
    break
