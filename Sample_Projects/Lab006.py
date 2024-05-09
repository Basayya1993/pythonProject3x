# WAP to denote the grade for respective percentage
# A: 90-100
# B: 75- 90
# C: 65-75
# D: Below 65

grade =int(input("percenatge of candidte:"))

if 90 <= grade <= 100:
 print("The Grade is A")
elif 75 <= grade <=90:
    print("Grade is B")
elif 65 <= grade <=75:
    print("Grade is C")
elif 35 <= grade <=65:
    print("Grade is D")

else:
    print("FAIL")
