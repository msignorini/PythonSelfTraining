# String operators
# split()
frase = "oggi non piove"
fraseSplit = frase.split()
print(fraseSplit)
print(frase.capitalize())
print(frase.upper())
#print(dir(frase)) lista dei metodi

# input
age = input("Insert your age: ")
print("You type:", age)

# list and IF
fruit = ["banana", "apple", "orange"]
if "peperone" in fruit:
    print("It is!")
else:
    print("It isn't!")

# function
def mySum(val1, val2):
    return val1 + val2

print(mySum(3,5))



