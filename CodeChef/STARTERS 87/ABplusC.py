# AUTHOR :: RAHUL MISTRY
# DATE   :: 28 / 04 / 2023
for i in range(int(input())):
    n = int(input())

    if n == 1:
        print(-1)
    elif n <= 10**6 + 1:
        print(1, n - 1, 1)

    else:
        x = n % 10 ** 6
        y = n // 10 ** 6
        if x != 0:
            print(10**6, y, x)
        else:
            print(10**6, y - 1, 10**6)
