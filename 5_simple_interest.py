principal, rate, time = map(float, input().split())

# Calculate interest

interest = (principal * rate * time) / 100

print("{:.6f}".format(interest))