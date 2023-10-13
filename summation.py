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
