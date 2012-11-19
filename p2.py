x = [2]
i = [1,2,3]
while i[2] < 4000000:
    if i[2] % 2 == 0:
        x.append(i[2])
    i[0] = i[1]
    i[1] = i[2]
    i[2] = i[0]+i[1]
print sum(x)
