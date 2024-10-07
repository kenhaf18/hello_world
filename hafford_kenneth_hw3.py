#4-6
for value in range(1,20,2):
    print(value)

#4-7
for value in range(3,31,3):
    print(value)

#4-8
cubed = []
for number in range(1, 11):
    cube = number**3
    cubed.append(cube)

for cube in cubed:
    print(cube)

#4-9
cubed = [number**3 for number in range(1,11)]

for cubed in cubed:
    print(cubed)

#Fibonacci Challenge
#0, 1, 1, 2, 3, 5, 8, 13.

a = 0
print(a)
b = 1
print(b)
for i in range(18):
    c = a + b
    print(c)
    a = b
    b = c