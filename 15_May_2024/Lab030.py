#printing the pyramid

x = int(input("Type the number:"))

for i in range (x):

    for j in range (i+1):
        print("*", end = "")
    print('')
for i in range (x, 0,-1):

    for j in range (i):
        print("*", end ="")
    print('')

