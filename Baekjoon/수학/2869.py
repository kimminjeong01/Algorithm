# 2023/03/21
# 달팽이는 올라가고 싶다

import math
import sys

a,b,v = map(int, sys.stdin.readline().split())

day = (v-b)/(a-b)
print(math.ceil(day))