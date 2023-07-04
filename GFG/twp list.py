l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]
res = []
for i in l1:
    if i not in res:
        res.append(i)
for j in l2:
    if j not in res:
        res.append(j)
print(res)