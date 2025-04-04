nums = [4, 60, 3, 1, 5, 9, 10]

i = 0
j = 0
aux = 0

for i in range(len(nums)):
    if i < 7:
        for j in range(len(nums)):
            if nums[i] < nums[j]:
                aux = nums[i]
                nums[i] = nums[j]
                nums[j] = aux

print(nums)
look = int(input("Number Query: "))
found = False

start = 0
end = 6



for i in range(len(nums)):
    if found == False:
        middle = round((start+ end) /2)
        if nums[middle] == look:
            print("found")
            found = True
            break
        elif nums[middle] < look:
            start = middle
        elif nums[middle] > look:
            end = middle
    
if found == False:
    print("not found!")