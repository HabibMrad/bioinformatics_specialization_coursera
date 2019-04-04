# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 21:46:32 2019

@author: hugo_
"""

text='GAGCCACCGCGATA'
def calcSkew(text):
    t=text[0]
    skew=[0]
    if t=='G':
        skew.append(1)
    elif t=='C':
        skew.append(-1)
    else:
        skew.append(0)
    for i in range(1,len(text)):
        #i=3
        t=text[i]
        if t=='G':
            skew.append(skew[i]+1)
        elif t=='C':
            skew.append(skew[i]-1)
        else:
            skew.append(skew[i])
     
    return ' '.join(str(s) for s in skew)