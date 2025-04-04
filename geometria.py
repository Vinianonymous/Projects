def perimetro(lados):
    sum = 0
    for i in range(lados):
        sum += int(input(f"Medida em CM do lado {i+1}: "))

    print(f"Perimetro: {sum}")

def area():
    forma = input("Nome da forma: ")

    match forma:
        case "quadrado":
            print(f"Area: {int(input("Lado: "))^2}cm²")
        case "retangulo" | "paralelogramo":
            print(f"Area: {int(input("Base: "))*int(input("Altura"))} cm²")
        case "triangulo":
            print(f"Area: {int(input("Base: ")) * int(input("Altura: ")) / 2} cm²")
        case "poligono": 
            if input("Você sabe a apotema e a medida dos lados? ") == "Y":
                print(f"Area: {int(input("Apotema: ")*perimetro(input("Lado:"))/2)} cm²")
        case _:
            print("ERRO: NENHUMA FORMA VÁLIDA ENCONTRADA")

        #Dava pra colocar mais né ;(





def main():

    lados = int(input("Lados: "))
    perimetro(lados)
    area()


main()
    


