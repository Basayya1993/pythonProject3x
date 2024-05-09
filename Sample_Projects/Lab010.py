#Fibonacci Series
# Out: 0 1 1 2 3 5 8 13 21 ......

a, b = 0, 1
while a < 10:
    print(a, end=" ")
    a, b = b, a+b


