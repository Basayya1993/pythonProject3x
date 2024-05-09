
x = int(input("Factorial of x value: "))

if x < 0:
    print ("Fact")
elif x == 0:
    print ("Fact:",1)
else :
    fact =1
    for i in range (1, x+1):
       fact = fact * i
print("Factorial of x is :", fact)






