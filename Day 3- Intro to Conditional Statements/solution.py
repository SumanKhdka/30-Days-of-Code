import math
import os
import random
import re
import sys

weird = False
N = int(input().strip())
if (N % 2 == 1) or (N % 2 == 0 and N >= 6 and N <= 20):
    weird = True
    
if weird:
    print("Weird")
else:
    print("Not Weird")