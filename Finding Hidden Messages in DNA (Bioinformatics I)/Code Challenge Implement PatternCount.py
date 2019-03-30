# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 19:15:57 2019

@author: S80240
"""
"""
PatternCount(Text, Pattern)
        count ← 0
        for i ← 0 to |Text| − |Pattern|
            if Text(i, |Pattern|) = Pattern
                count ← count + 1
        return count
"""
  
def patternCount(text,pattern):
    count=0
    len_text=len(text)
    len_pattern=len(pattern)
    for i in range(len_text-len_pattern):
        if text[i:i+len_pattern] ==  pattern:
            count=count+1
    return count

"""
FrequentWords(Text, k)
        FrequentPatterns ← an empty set
        for i ← 0 to |Text| − k
            Pattern ← the k-mer Text(i, k)
            Count(i) ← PatternCount(Text, Pattern)
        maxCount ← maximum value in array Count
        for i ← 0 to |Text| − k
            if Count(i) = maxCount
                add Text(i, k) to FrequentPatterns
        remove duplicates from FrequentPatterns
        return FrequentPatterns
"""


def frequentWords(text,k):
    count={}
    for i in range(len(text)-k):
        pattern = text[i:i+k]
        if pattern not in count.keys():    
            count[pattern]=patternCount(text,pattern)
        else:
            count[pattern]=count[pattern]+patternCount(text,pattern)
    max_count=max(count.values())
    frequentPatterns = [pattern for pattern in count if count[pattern] == max_count]
    return frequentPatterns
    


text="GGGGCTTTTCCGCAAGGCTCCTGAACCTGGCCTGGGGCTTTGGGGCTTTTCCGCAAGTCCGCAAGGGGGCTTTTCCGCAAGGGGGCTTTGAGTTGCATGAGTTGCATGGGGCTTTACCTGGCCTACCTGGCCTACCTGGCCTGAGTTGCATGCTCCTGATCCGCAAGTCCGCAAGGGGGCTTTGGGGCTTTACCTGGCCTGCTCCTGATCCGCAAGGAGTTGCATGAGTTGCATACCTGGCCTGGGGCTTTGCTCCTGAACCTGGCCTGCTCCTGAACCTGGCCTGGGGCTTTTCCGCAAGGCTCCTGATCCGCAAGGAGTTGCATGAGTTGCATACCTGGCCTGCTCCTGAGGGGCTTTGAGTTGCATTCCGCAAGGCTCCTGATCCGCAAGACCTGGCCTGCTCCTGAGGGGCTTTGCTCCTGAGCTCCTGAGCTCCTGATCCGCAAGGCTCCTGAGGGGCTTTGAGTTGCATTCCGCAAGACCTGGCCTGAGTTGCATGAGTTGCATGAGTTGCATACCTGGCCTTCCGCAAGGGGGCTTTTCCGCAAGTCCGCAAGACCTGGCCTGGGGCTTTGGGGCTTTGGGGCTTTTCCGCAAGGAGTTGCATGGGGCTTTGCTCCTGAGGGGCTTTGAGTTGCATACCTGGCCTTCCGCAAGGAGTTGCATTCCGCAAGGCTCCTGAACCTGGCCTGCTCCTGATCCGCAAGGGGGCTTTACCTGGCCTGAGTTGCATGCTCCTGATCCGCAAGGAGTTGCATGGGGCTTTGGGGCTTTTCCGCAAGGCTCCTGAGAGTTGCAT"
k=11
for pat in frequentWords(text,k):
    print(pat)