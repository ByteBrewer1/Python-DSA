string = input()

low_c = 0
upp_c = 0
for char in string:
    if char.islower():
        low_c += 1
    else:
        upp_c += 1

if low_c >= upp_c:
    print(string.lower())
else:
    print(string.upper())
