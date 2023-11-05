numbers = {'M': 1000, 'D': 500,
           'C': 100, 'L': 50,
           'X': 10, 'V': 5, 'I': 1}
n = "CIV"
a = 0
i = 0
for i in range(len(n)-1):
    if numbers[n[i]] < numbers[n[i + 1]]:
        a += numbers[n[i + 1]] - numbers[n[i]]
    else:
        a += numbers[n[i]]
print(a)
