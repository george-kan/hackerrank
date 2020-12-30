# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 08:16:03 2020

@author: George
"""

from collections import Counter
from itertools import groupby, permutations, combinations
from datetime import datetime
from operator import itemgetter
import re
from fractions import Fraction
from functools import reduce


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
        


### Merge the tools -- split string into substrings and take the unique values
# Note that we need the counter or the dictionary in order to preserve the order, otherwise set would do

inp = 'AABCAAADA'
k = 3

chunks = len(inp)//k
chunk_counter = 0

for chunk in range(chunks):
    print(''.join(Counter(inp[(chunk_counter*k):((chunk_counter+1)*k)])))
    chunk_counter += 1
    
### Time Delta -- find time difference in seconds

inp1 = 'Sun 10 May 2015 13:54:36 -0700'
inp2 = 'Sun 10 May 2015 13:54:36 -0000'

time_diff = datetime.strptime(inp2, '%a %d %b %Y %H:%M:%S %z') - datetime.strptime(inp1, '%a %d %b %Y %H:%M:%S %z')
time_diff.total_seconds()




### No Idea! -- Count the number of elements in a list that appear in two other arrays

# Since you only check if an element is in arr1 or arr2 you can do set arr1 and set arr2
inp = [1, 5, 3]
arr1 = [3, 1]
arr2 = [5, 7]

tot_score = 0
inp = Counter(inp)

for elem, value in inp.items():
    if elem in arr1:
        tot_score += value
    elif elem in arr2:
        tot_score -= value

sum([(x in arr1) - (x in arr2) for x in inp])



### Word Order -- Count the # of appearances of words in a list

inp = ['bcdef', 'abcdefg', 'bcde', 'bcdef']
counts = Counter(inp) # Counter maintains input order so this should be sufficient for the purposes

' '.join([str(value) for value in counts.values()])



### Compress the String! -- Find groups of consequtive letters in a string

inp = '1222311'
groups = groupby(inp)

for k, group in groups:
    print(k, len(list(group)))
    print(list(group)) 



### Company Logo -- Find the 3 most common characters in a string
# Sorting a dictionary (or iterable) based on values. Sorted function returns a list so we can slice it
inp = 'aabbbccde'

counts = Counter(inp)
sorted_counts = sorted(counts.items(), key = lambda x: (-x[1], x[0]))

[print(x[0], x[1]) for x in sorted_counts]



### Traingle quest 2 -- Print a palindrome

k = 5

for i in range(1,int(k)+1): 
    print(''.join([str(x) for x in range(1,i+1)]) + ''.join([str(x) for x in range(i-1, 0, -1)]))



### Itelables and iterators -- Find the permutations that contain a letter
k = 2
inp = 'a a c d'.split()

combs = list(combinations(inp, k))
a_perc = sum([True for x in combs if 'a' in x]) / len(combs)



### Athlete sort -- Sort nested list by certain element

inp = [[10, 2, 5],
       [7, 1, 0],
       [9, 9, 9],
       [1, 23, 12],
       [6, 5, 9]]

k = 2

sorted(inp, key = itemgetter(k))



### ginortS -- Different types of sorting a string

inp = 'Sorting1234'

''.join(sorted(re.findall('[a-z]', inp))) + ''.join(sorted(re.findall('[A-Z]', inp))) + ''.join(sorted(re.findall('[0-9]', inp)))


### Validating Email Addresses With a Filter -- Regex matches

inp = 'ha-r]sh@gmail.com'

re.match('^(\w|-)*@[a-zA-Z0-9]*\\..{3}$', inp)



### Reduce Function -- Reduce Function

inp = [1,2,4,5]

reduce(lambda x,y : x*y, inp) # 1*2*4*5



### Regex Substitution -- Using re.sub replace multiple patters in the word

html = """
if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.
"""

def dashrepl(matchobj):
     if matchobj.group(0) == '&&' : return 'AND'
     else: return 'OR'
     
re.sub('(?<=\s)(\\|\\||&&)(?=\s)', dashrepl, html, count = 0)



### Validating Credit Card Numbers -- Regex for numbers

#It must start with a 4, 5 or 6.
#It must contain exactly 16 digits.
#It must only consist of digits (0-9).
#It may have digits in groups of 4, separated by one hyphen "-".
#It must NOT use any other separator like ' ' , '_', etc.
#It must NOT have 4 or more consecutive repeated digits.

string = '5122-2368-7954-3214'
string = '5122-2268-7954-3214'
if '-' in string:
    if re.match('(\d{4}-){3}\d{4}', string):
        string = re.sub('-', '', string)
        
re.match('^[456]((\d)(?!\\2{3})){15}$', string)

## This works as follows: The first group (\\1) is the first parenthesis which is not finished at the time of the lookahead
## The second capturing group is the \d inside the parenthesis and that's why we use it at the lookahead



### Words Score -- Score words based on how the number of vowels it contains

inp = 'programming is awesome'
inp = inp.split(' ')

[2 if len(re.findall('[aeiouy]', x))%2==0 else 1 for x in inp]



### Default arguments -- Mutable default arguments in python functions

def append_to(element, to=[]):
    to.append(element)
    return to

append_to(12)
append_to(14)

# The list in the default argument is a mutable object. Python initialises it to [] only the first time the function is called
# Afterwards the values just simply increase 

def append_to2(element, to=None):
    if to == None:
        to = []
    to.append(element)
    return to

append_to2(12)
append_to2(14)
