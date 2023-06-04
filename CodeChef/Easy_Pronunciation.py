for _ in range(int(input())):
    n = int(input())
    s = input()

    count = 0
    is_easy = True
    for char in s:
        if char not in 'aeiou':
            count += 1
            if count >= 4:
                is_easy = False
                break
        else:
            count = 0
    if is_easy:
        print("YES")
    else:
        print("NO")
