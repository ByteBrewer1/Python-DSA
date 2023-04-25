
#! AUTHOR :: RAHUL MISTRY
#* DATE   :: 09/04/2023

def find_largest(matrix):
    max_value = float('-inf')
    for row in matrix:
        max_row = max(row)
        if max_row > max_value:
            max_value = max_row
    return max_value


m, n = map(int, input().split())

matrix = []
for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)
largest = find_largest(matrix)
print(largest)