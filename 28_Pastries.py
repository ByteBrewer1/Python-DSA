
#! AUTHOR :: RAHUL MISTRY
#* DATE   :: 08/04/2023

# Function to serve customers and return appropriate message
def serve_customers(n, q, pastries):
    for i in range(q):
        pastry_count = pastries[i]
        if n >= pastry_count:
            n -= pastry_count
            print("Enjoy your dessert!")
        else:
            print("Sorry, we are all out!")

# Taking input
n, q = map(int, input().split())
pastries = []
for i in range(q):
    pastries.append(int(input()))

# Calling the function
serve_customers(n, q, pastries)
