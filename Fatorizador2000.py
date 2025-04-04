

print("Não dava pra tu calcular isso sozinho?")
opstring = input("Operação: ")
fat = opstring.split()
print(fat)

if "^2" in fat[0] and len(fat) == 5:

    print("Equação quadratica detectada")

    if fat[0].split("x")[0].isnumeric():
        print("Bhaskara")
    else:
        print("Trinomio da forma x^2+bx+c")

elif len(fat) == 3 and fat[1] =="-" and :
    print("Binomio detectado")



    

