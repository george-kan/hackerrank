# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 08:16:03 2020

@author: George
"""

from collections import Counter
from itertools import groupby


### Minion -- find the number of substrings starting with a letter
inp = 'BANANA'
v = 0
c = 0

for ind in range(len(inp)):
    if inp[ind] in 'AEIOUY':
        v += len(inp) - ind
    else:
        c += len(inp) - ind
        
### Minimum absolute difference in array
        
inp = [-59, -36, -13, 1, -53, -92, -2, -96, -54, 75, 75]
new_inp = Counter(sorted(inp))
keys = list(new_inp.keys())

abs_valu = max(new_inp) - min(new_inp)
for ind in range(len(keys)):
    if new_inp[keys[ind]] > 1:
        abs_valu = 0
        break
    if abs(keys[ind] - keys[ind+1]) < abs_valu:
        abs_valu = abs(keys[ind] - keys[ind+1])
        

### Merge the tools -- 