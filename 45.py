a = [2,1,3,6,5,7,10]
for i in a:
    if i%2 != 1:
        a.remove(a.index(i))
print(a)
