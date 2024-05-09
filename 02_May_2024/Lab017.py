list = [1,2,4,6]

print("Give my numbers in list:",list)
print("Give my numbers in list:",list[0])


list[1] = 15
print("Give my numbers in list:",list)
print("Give my numbers in list:",list[0],list[2])

list.append(7)
print("Give my numbers in list:",list)

list.extend([7,5])
print("Give my numbers in list:",list)
