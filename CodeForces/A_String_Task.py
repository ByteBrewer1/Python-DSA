string = input().strip().lower()

vowels = {'a', 'e', 'i', 'o', 'u'}
new_string = ''

for letter in string:
    if letter in vowels:
        continue
    else:
        new_string += '.' + letter

print(new_string)
