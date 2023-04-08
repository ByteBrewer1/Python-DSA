
#! AUTHOR :: RAHUL MISTRY
#* DATE   :: 08/04/2023

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

T = int(input())

for i in range(T):
    s = input().strip()
    ans = count_vowels(s)
    print(ans)