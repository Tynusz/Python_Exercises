a, b, c = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], [], []
C = int(input("give a number"))
for i in range(0,len(a)):
    if a[i] < 5:
        b.append(a[i])
    c.append(a[i]-C)
    
print(b)

print(c)
