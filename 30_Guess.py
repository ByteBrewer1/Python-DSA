
#! AUTHOR :: RAHUL MISTRY
#* DATE   :: 09/04/2023

bd = int(input())
for _ in range(31):
    num = int(input())
    if num == bd:
        print("Correct Guess")
        break
    else:
        print("Incorrect Guess")