n = int(input())
color = input()
cnt = 0
for i in range(1, len(color)):
    if color[i-1] == color[i]:
        cnt += 1
print(cnt)
