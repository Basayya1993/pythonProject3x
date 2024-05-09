name = input("enter name:")

length = len(name)
reverse =""

for i in range (length-1,-1):
    reverse+=name[i]
    print(reverse)

