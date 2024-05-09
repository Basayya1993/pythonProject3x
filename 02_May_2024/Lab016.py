#str = "Basu"
#Using function
def str_name(str):
    rev_str = ""
    for i in str:
        rev_str = i + rev_str
    print(rev_str)

rev_str = str_name("Basayya")

#Normal Reversal string
str = input("String Name :")
rev_str = ""
for i in str:
    rev_str = i + rev_str

print("After reversal:",rev_str)