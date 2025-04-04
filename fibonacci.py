def main():
    num = int(input("Number: "))
    fibonacci(num)

def fibonacci(num):
    cont = 1

    act = 1
    prev = 0
    apr = 0

    while cont <= num:
        print(act, sep="")
        apr = prev
        prev = act
        
        act = prev + apr

        
        cont +=1


main()
