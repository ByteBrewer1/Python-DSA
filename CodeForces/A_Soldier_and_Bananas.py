k, n, w = map(int, input().split())

total_money_required = 0

for i in range(1, w+1):
    money = i * k
    total_money_required += money

if total_money_required > n:
    print(total_money_required - n)
else:
    print(0)
