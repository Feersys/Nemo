#  I V X C D
n = input(" Input: ")
a = 25
b = {100: 0,
     50: 0,
     10: 0,
     5: 0,
     1: 0}
for k in b:
    x = a // k
    b[k] = x
    a = a % k


print(b)
