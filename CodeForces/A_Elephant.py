
x = int(input())

dist = 0
step = 0
while dist < x:
    if x - dist >= 5:
        dist += 5
        step += 1
    elif x - dist >= 4:
        dist += 4
        step += 1
    elif x - dist >= 3:
        dist += 3
        step += 1
    elif x - dist >= 2:
        dist += 2
        step += 1
    else:
        dist += 1
        step += 1
print(step)
