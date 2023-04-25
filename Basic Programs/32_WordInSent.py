
#! AUTHOR :: RAHUL MISTRY
#* DATE   :: 09/04/2023

def count_words(line):
    words = line.split(" ")
    num_words = len(words)
    return num_words

line = input()
num_words = count_words(line)
print(num_words)