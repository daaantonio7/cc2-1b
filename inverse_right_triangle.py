# NO. 3
num2 = [1, 2, 3, 4, 5]
y = 4
x = 0 # loop counter
while x < 5:
    for i in num2:
        print(i, end=" ")
    print("")
    del num2[y] # removes value from list
    y -= 1
    x += 1 # stops loop

