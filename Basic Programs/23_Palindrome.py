
#! AUTHOR :: RAHUL MISTRY
#* DATE   :: 07/04/2023

def is_palindrome(word):
    # Remove any whitespaces and make all to lowercase
    word = word.strip().lower()
    if word == word[::-1]:
        return True
    else:
        return False



T = int(input())

for i in range(T):
    word = input()
    result = is_palindrome(word)
    print(result)

