array = [["Na", 20],["Jp", 48], ["Vr", 63]]

for i in range(len(array)):
        print(f"{array[i][0]} | {array[i][1]}")



#Transpose:an
#List comprehension
ta = [ [item[0] for item in array], [item[1] for item in array] ]
print(ta)
