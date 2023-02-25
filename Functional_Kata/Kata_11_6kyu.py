def pyramid(n):
    res = []
    for i in range(n):
        lj = []
        lj.append(1)
        for j in range(i):
           lj.append(1)
        res.append(lj)
    return res


print(pyramid(3))