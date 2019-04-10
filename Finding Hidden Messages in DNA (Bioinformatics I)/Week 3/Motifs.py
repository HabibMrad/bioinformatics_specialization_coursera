# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 20:44:20 2019

@author: hugo_
"""
"""
MotifEnumeration(Dna, k, d)
        Patterns ← an empty set
        for each k-mer Pattern in Dna
            for each k-mer Pattern’ differing from Pattern by at most d mismatches
                if Pattern' appears in each string from Dna with at most d mismatches
                    add Pattern' to Patterns
        remove duplicates from Patterns
        return Patterns
"""
def hammingDistance(p,q):
    min_len = len(p)
    q_len=len(q)
    if q_len<min_len:
        min_len=q_len
    distance=0
    for i in range(min_len):
        if p[i]!=q[i]:
            distance+=1
    return distance

def approximatePatternMatching(pattern, text, d):
    positions = []
    len_text=len(text)
    len_pattern=len(pattern)
    for i in range(len_text-len_pattern+1):
        qattern = text[i:i+len_pattern]
        if pattern == qattern or hammingDistance(pattern,qattern)<=d :
            positions.append(str(i))
    return positions
            
    
def approximatePatternCount(pattern, text, d):
    positions=approximatePatternMatching(pattern, text, d)
    return len(positions)

def neighbors(pattern, d):
        if d == 0:
            return pattern
        if len(pattern) == 1 :
            return ['A', 'C', 'G', 'T']
        neighborhood = []
        suffixNeighbors = neighbors(pattern[1:], d)
        for text in suffixNeighbors:
            if hammingDistance(pattern[1:], text) < d:
                for x in ['A', 'C', 'G', 'T']:
                    neighborhood.append(x + text) 
            else:
                neighborhood.append(pattern[0] + text)
        return neighborhood

    
def motifEnumeration(dna, k, d):
        patterns = set()
        for single_dna in dna:
            for i in range(len(single_dna)-k+1):
                pattern=single_dna[i:i+k]
                neighborhood=neighbors(pattern, d)
                for neighbor in neighborhood:
                    every_string=True
                    for single_dna_2 in dna:                
                        if approximatePatternCount(neighbor, single_dna_2, d)==0:
                            every_string=False
                    if every_string:
                        patterns.add(neighbor)
        return patterns
    
k=5
d=1
dna=['ATGTATACCGACCAGTACCAACATT','CGTCTTGTCCGCGCGATCAGAAAGT','AAGACACCACACCAGCTGACGGCCG','CATCTACCAGTGGATTGCAAATTGC','GCTTGATCCGCTGCATTTGTACCAG','ACCAGTGGCATCTCTATCTCATAGA']  
motifEnumeration(dna, k, d)

motifs = [
"TCGGGGGTTTTT",
"CCGGTGACTTAC",
"ACGGGGATTTTC",
"TTGGGGACTTTT",
"AAGGGGACTTCC",
"TTGGGGACTTCC",
"TCGGGGATTCAT",
"TCGGGGATTCCT",
"TAGGGGAACTAC",
"TCGGGTATAACC"
]
        
def nucleotideDic(motifs):
    dicList=[]
    for i in range(len(motifs[0])):
        dic = {'A':0,'C':0,'G':0,'T':0}
        dicList.append(dic)
    return dicList

def countMotifs(motifs):
    profiles_list= nucleotideDic(motifs)
    for motif in motifs:
        for i in range(len(motif)):
            nucleotide=motif[i]
            nucleotide_dic=profiles_list[i]
            nucleotide_dic[nucleotide]=nucleotide_dic[nucleotide]+1
            profiles_list[i]=nucleotide_dic
    return profiles_list

countMotifs(motifs)

def profileMotifs(motifs):
    countDic=countMotifs(motifs)
    denominator=int(len(motifs))
    for dic in countDic:
        for key in dic.keys():
            dic[key]=dic[key]/denominator
    return countDic

profileMotifs(motifs)

from math import log

def entropy(motifs):
    profile=profileMotifs(motifs)
    entropy=0
    entropy_list=[]
    for p in profile:
        score0=0
        for nucleotide in p.keys():
            score=p[nucleotide]
            if score > 0 and score<1:
                score0=score0+score*log(score,2)
                entropy=entropy-score*log(score,2)              
        entropy_list.append(score0*-1)
    return entropy

entropy(motifs)


        
    
        