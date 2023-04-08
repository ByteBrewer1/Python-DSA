# AUTHOR :: RAHUL MISTRY
# DATE   :: 07/04/2023

PI = 3.14
rate = 40

radius, height = map(float, input().split())

volume = (PI * (radius * radius) * height) # in cm^3

# convert cm^3 in to litre we divide it by 1000
volume_litre = volume / 1000;

amount = volume_litre * rate

print("{:.2f}".format(amount))