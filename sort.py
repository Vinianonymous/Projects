
names = ["Zara", "Liam", "Emma", "Noah", "Olivia", "Mason", "Sophia", "Aiden", "Isabella", "Lucas"]

i = 0
sw = 0

while i <= len(names):
    if i <= 9:
        j = 0
        while j <= len(names):
            if j <= 9:
                if names[j] > names[i]:
                    sw = names[i]
                    names[i] = names[j]
                    names[j] = sw

            j+= 1
    i +=1

print(names)
i = 0
j = 0

search = input("Desired name: ")
found = False

for i in range(len(names)):
    start = 0
    end = 9
    middle = round(((start+end)/2))

    if found == False:
        for j in range(len(names)):
            middle = int((start+end)/2)

            if names[middle] == search:
                print(f"Name Found at index {middle}")
                found = True
                break
            elif names[middle] > search:
                end = middle + 1
            elif names[middle] < search:
                start = middle - 1
    else:
        break