n = input().strip()
lucky_count = n.count('4') + n.count('7')
if lucky_count == 4 or lucky_count == 7:
    print("YES")
else:
    print("NO")
