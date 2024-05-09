def hello_name(*arg):
    for args in arg:
        print(args)

args = hello_name("Basu","Basayya")

num = int(input("Factorial of :"))
if num < 0:
    print("Fact")
elif num == 0:
    print(1)
else:
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print(fact)


