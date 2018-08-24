# [] = list
# () = tuple
# {} = dictonary


# List
l = [1, "ciao", 7.81]
print(l)
l.append("zeta")
print(l)
l[1] = 14
print(l)

# dictonary
d = {"apples": 5, "pears": 2, "oranges": 9}
print(d)
print(d["apples"])
d["banana"] = 16
print(d)


# loops
for i in range(5):
    print(i)

for i in l:
    print(i)

i = 0
while i < 5:
    print(i)
    i += 1

# unpacking
a, b, c = [1, 2, 3]
