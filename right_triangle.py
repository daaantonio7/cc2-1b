# NO. 1

num = []
y = 1 
x = 0 # loop counter

while x < 5:
    num.append(y) # adds value to list
    for i in num:
        print(i, end=" ")
    print("")
    y += 1
    x += 1 # stops while loop
