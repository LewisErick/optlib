# 1D Bin Packing Utilities
# by lewiserick

import numpy as np
from math import sqrt

def f1(restantes):
    print('f1: {} / {} = {}'.format(sum(restantes),
        len(restantes),
        sum(restantes) / len(restantes)))
    return sum(restantes) / len(restantes)

def f2(restantes):
    print('f2: {}'.format(np.std(restantes)))
    return np.std(restantes)

def f3(restantes):
    print('f3: {} / {} = {}'.format(sum([x for x in restantes if x > 7.5]),
        sum(restantes),
        sum([x for x in restantes if x > 7.5]) / sum(restantes)))
    return sum([x for x in restantes if x > 7.5]) / sum(restantes)

def distance(x1, x2):
    return sqrt((x1[0]-x2[0])**2 + (x1[1]-x2[1])**2 + (x1[2]-x2[2])**2)

def evaluate_funcs(x1, funcs_x):
    for idx, x2 in funcs_x:
        print('{} -> {}'.format(idx, distance(x1, x2)))

# Bin Packing
restantes = [8, 1, 3, 1, 1, 9, 7, 4, 10, 1, 5, 4, 8, 8, 2]
# ff - first first
# bf - best fit
# wf - worst fit
# awf - almost worst fit
funcs_x = [['ff', [4.0, 2, 0.5]],
            ['bf', [5.0, 0, 0.0]],
            ['wf', [5.5, 2, 0.4]],
            ['awf', [6.5, 3, 0.3]]]
x1 = [f1(restantes), f2(restantes), f3(restantes)]
