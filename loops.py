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

# NO. 2

# Variables
inpt = input("Enter value here: ")
userinput = int(inpt)
sum = 0
Formula_list = []

# Prints the input value
print(f"Input: {userinput}")

#Loop for outputting formula
for i in range(userinput):
    i += 1
    Formula_list.append(i)
else:
    print("Formula:", end=" ")
    print(*Formula_list, sep='+')

# Loop for getting output
for i in range(userinput): 
    i += 1
    sum = sum + i
else:
    print(f"Output: {sum}")


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




   
    