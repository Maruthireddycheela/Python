# write a program for fibonacci series

a = 0
b = 1
print(a)
print(b)
for i in range(2, 10):
    sum = a+b
    print(sum)
    a = b 
    b = sum

