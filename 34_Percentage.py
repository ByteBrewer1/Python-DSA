
#! AUTHOR :: RAHUL MISTRY
#* DATE   :: 09/04/2023

def calculate_percentage(n, marks):
    total_marks = n * 80
    sum_marks = sum(marks)
    percentage = ( sum_marks / total_marks ) * 100
    result = "{:.2f}%".format(percentage)
    return result

n = int(input())
marks = []
for i in range(n):
    mark = int(input(format(i+1)))
    marks.append(mark)

percentage = calculate_percentage(n, marks)
print(percentage)