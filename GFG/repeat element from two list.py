l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]
res = []
for i in l1:
    for j in l2:
        if i == j:
          res.append(i)
print(res)