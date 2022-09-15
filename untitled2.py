# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 16:55:55 2022

@author: jomg0
"""

from itertools import permutations 
from itertools import combinations
n, m = map(int,input().split())
arr = list(map(str,range(1,n+1)))
#print(arr)
#print('\n'.join(list(map(' '.join,permutations(arr,m)))))
print('\n'.join(list(map(' '.join.combinations(arr,m)))))
