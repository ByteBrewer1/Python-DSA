# AUTHOR :: RAHUL MISTRY
# DATE   :: 28 / 04 / 2023

import os
import math
import re

for i in range(int(input())):
    x, y = map(int, input().split())
    price_x = x * 5
    price_y = y * 2 + x
    if price_x > price_y:
        print(price_y)
    else:
        print(price_x)
