import os
import math
import re

string = input().strip()

if '1111111' in string or '0000000' in string:
    print("YES")
else:
    print("NO")
