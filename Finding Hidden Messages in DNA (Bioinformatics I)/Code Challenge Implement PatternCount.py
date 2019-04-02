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
    for i in range(len_text-len_pattern+1):
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
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        if pattern not in count.keys():    
            count[pattern]=patternCount(text,pattern)
    max_count=max(count.values())
    frequentPatterns = [pattern for pattern in count if count[pattern] == max_count]
    #return frequentPatterns
    return {max_count:frequentPatterns}
    

text="GGGGCTTTTCCGCAAGGCTCCTGAACCTGGCCTGGGGCTTTGGGGCTTTTCCGCAAGTCCGCAAGGGGGCTTTTCCGCAAGGGGGCTTTGAGTTGCATGAGTTGCATGGGGCTTTACCTGGCCTACCTGGCCTACCTGGCCTGAGTTGCATGCTCCTGATCCGCAAGTCCGCAAGGGGGCTTTGGGGCTTTACCTGGCCTGCTCCTGATCCGCAAGGAGTTGCATGAGTTGCATACCTGGCCTGGGGCTTTGCTCCTGAACCTGGCCTGCTCCTGAACCTGGCCTGGGGCTTTTCCGCAAGGCTCCTGATCCGCAAGGAGTTGCATGAGTTGCATACCTGGCCTGCTCCTGAGGGGCTTTGAGTTGCATTCCGCAAGGCTCCTGATCCGCAAGACCTGGCCTGCTCCTGAGGGGCTTTGCTCCTGAGCTCCTGAGCTCCTGATCCGCAAGGCTCCTGAGGGGCTTTGAGTTGCATTCCGCAAGACCTGGCCTGAGTTGCATGAGTTGCATGAGTTGCATACCTGGCCTTCCGCAAGGGGGCTTTTCCGCAAGTCCGCAAGACCTGGCCTGGGGCTTTGGGGCTTTGGGGCTTTTCCGCAAGGAGTTGCATGGGGCTTTGCTCCTGAGGGGCTTTGAGTTGCATACCTGGCCTTCCGCAAGGAGTTGCATTCCGCAAGGCTCCTGAACCTGGCCTGCTCCTGATCCGCAAGGGGGCTTTACCTGGCCTGAGTTGCATGCTCCTGATCCGCAAGGAGTTGCATGGGGCTTTGGGGCTTTTCCGCAAGGCTCCTGAGAGTTGCAT"
k=11
for pat in frequentWords(text,k):
    print(pat)
    
    
def reverseComplement(pattern):
    dic ={'A':'T','T':'A','C':'G','G':'C'}
    new_pattern=[]
    n=""
    for l in pattern:
        new_pattern.append(dic[l])
        n=n+l
    new_pattern.reverse()
    return ''.join(new_pattern)
    
pattern ="GACACAGATAGAGTTAACCGGTCATGGGTCCGGGGACTAGGCGTGTAGTCCGCTAGTTGTAAACACGGAGACTTGTTAATTACACACTCAATATCACGCGTTACCTCTCAACTCGCGGTATTTAGGGCAGGACCCAGAAACTGGGTTTCAAACAAGGAGCGGTACTTCCCTAAGATACTGGAATGTTTTGCACTCAATTAGGACTGTCTCCCAGACCTCCGCTATCCACAACCCTCACTTGATTTTCTGATATAAACAGCGTCCTACCTAAGGACCCATGGCATACCCAAGCGCGAAGTGACGCCACTCATCCAGTCGGAAAGCACTTTACTCGAAAATTTTGGGATGAACTTAATGATCCTGTTCGTTTCAAGGCGAGTGAAGTCCGAGCGCTCCGTACACCGAAACAGGTTGTCTGGGGATAAGTCAGCTATTGTAGGTAGCTTCATCTTAGGACTCTATGGTGCCGCGATCTCTATACGCAGTTATCCCAAGGTGGAAAATGCGTGGGCTTTGCGCCACGACCAGTTTCTGACCGCGTTGAGTTGATCACGCCCACACCTTACTGCGGTATTTAATCGGCTCGCTTGCTGTGCTCACTCATGACAGAGAGTTGCGCCCCGGCGGCCGGTTGCCGCTAGCCAGTTTCAGAGGTAACATTATTCACTGATTTCCTTATCCTCCACTAGCCGCCTTAATACGCGTTCATTCAGTCAGGGGGTATACTATCTGTTAGTGTCGATTAACTTCGCACCACCTGTCAACAAGCTCTCCTAGGATCGGCCTGATGGATAATAGTGTGACTCTCGTCCGGTCCCGGGTGTATTAGGACATGCACCTACTTCCCAGATCTGGTAGACTGCAAGGCCACTCCGCGAGGTATGGAAAGGCGACACGAGTTCGCAATGCTCTTCCCCCACACAAATACTTCACAGAGATTAGACCATTCGGAGAGTCACACAAGTACATTTCCCCGTATAGGATAATACCCTCTTCTGAGTTTATTATATTGACTATAGGGAAAAATAAATGCTTTCATTATATCGATGAAGTATCAGTCCTCTCAATGTGGCTATGCGCAGTGGGGATAATTCCCAATTTTCAAGCTCGCGCATCGATCTATGCTGAAAAAAGAGTCTAAGTAAAGAGATTAAGACCGTACAAGCCGACCCCTGGGTTTACGACGAAGTTCTTTGGACTCAACTACCGGACTATACATGAACCTACTATCGCCGCATGCCGAACCCTTGAGGGGTGTATAACGGACTTTTAAAGGTCATAAGGTTTCTTGATACGATCAATCGTGATGTGGGGCGAAGAGGGTCGGTTGGGGGAATGACGTAGGTCTCTACCCTAGACGATGAACAGCCCCTCTTTGAGTATTATTTGTACCAAGATGAGGTGATTACGTCTTTTAACGAACCCATCGATCCAGAACATCACCATCCATCGTAATCTGCCTTTATGAGTATAGCAATGGGTTTCGACATCCATCCGCTGATAGTCCTCTGTTTCGCACCGTCCGTGTCCACCTGATAGTCGGTCCCGCTGCAGGGACTGAGGCCGCGATCTCGCCCTTATCCTTACTAGCGTTCTACTGTATAAGATGGTTTACTCCTCTAGTAGTCGTATCATCGATTTATGCCAATTTTAATGCGACCGGGTACAAAGGCATCAAGTAAAGCCGTCGTCGCAAACCGTAAAAACGGAATGTCTCACAGGCGGCTATGGATCCATTGACGCCGAGGTGGTCCCACGATTACTAATCTCTTTACTTTTCTGTTCAACTTAAACGGCGGTTTTCTACGAGGATACGCCCGTTAGATGGATTCATTGTGGCGTATTTCCATGAATCAGTTGGCGCTAAACCAGCATCGTTCCTATTGAAATTGTTACATCGGGCTAGCAAGCTACGCAACCCATCGGACTGGCCGATGTGCTACATCCGGAAATCTCTTAGATCCTCTACCTCTGATAAGTTTGCGATTGCAAGCGGGCTGATACGCTCCCGATACTAATGGCGCAAAGGTATGGGAGGAAGCGATGTGCGAGCCATCCAATCTTTTGATCCTCGATGCTCCCAACTCTGCGTGGGTTCGTGGACCCCTGTTAGAAAGCCGGTTGGATGCCTGAGTCAGGGACTTGCAAATAGGGGGGTACCTGAAGGCCCCGGGAGGAGTGCTTGGGGGTTGGAAACCACTCGGTGGGATGCGGACGACGCATAGACCTGCCAGCGCATCGGACACTTTTACTTCCGGGGCCCCCTCGCAAGAGCTTTTTGGTTGCGCAGCTTGCGAGTGATGTGGACGGGGTACTCGACCTTAATCAACAACTATGGCGCGGGAGTAAACTCGTCAGCACTGTCGATCACGTTTTCCGAAGGCTTAGCGAATGCCCTCTCGCAGGTTCTGTGCGATGTAGAATGCAGGGATGGACTCTATGGGCTCCCCTTGATGAGGCCGGGCCCCATCGATTGTCCATCGCACAAGAGGGGCGGGTTAAAAGATCCCCGGACGTGTCACTCACGATGCTCGACGGAGGCGGAGGAACGCACTAAAATACTGCTCTGAGAAGTGTTGTAGGAGTGGCGCTTGGCTAGTCTCGTCACCCTGGTGGCTAATGTTCGTATTTCCTGCCTCCGCTGACTAGACAACCAAAATGTGCGCTCTCTTTTGGTCAGAGGAGGAACGTGCATTCGGACGATGTCCCTCGACCACCTACAACTTGGTTTATGTCGCTCAACTCGACAGGTAATTAATGGACGGAGTACCGGAACTTGCTGGACACCGCTACCATGAGCCCCGTGCGTGGACTGCATTGTGACGCCTTTAGCCGCCATCAGCCCGACGCTCGCAGATACTTGCGAACAGTATCTAGTTAACACAACAATTATTGCCTCCGCCACAGGTAGGGGGCGACAGCTGAGATCTACCGCCACCCTTAATACCTGACCTAACCGTCCAACACGTGTTCCCGCCAGACAGCGGTTCCAACGCCCAAGATCACCGAGTACGACCGATAGCCTGAGGAGGGGAATATGTAATCCGATGTTCCAAGGGCAGCCCTTCCCGAACTATTAATGTAGTGGTGTTGAATGAGGCACCTCCAGTGAAACGTAATTTTGTTGCAAGCTCGTGTGGGCAGGCAACTAGAGACTCGCGAGAACGCATGGGCCGAGACGAAAGGCAATCCGAAACAGGGACCACGCCACACGACTGTACCCGTACGAGCGCCAAATGATAGACAAATACACCCTCGAGCTCAGCTTACGAACCCCGGAAGGACTATCCGATAGTGCTGCGACTCTATGCTACTATAGTATCAACTTTTCCGTCCGGAACAGGAGACAATAATGAAATATCCGGCCTAAGTATCCGTTTTGAAAAGTGAGCTTGGTGGACGTCCTTCCCGGCAGGCGATGTTTAGAGGATGTGAACCCTTGTTTATCTAGTGGCTTTTAAATGGCGCAACGGGCTTTCTCGATCTCGGGTCATTAATGTAGGCGTCCTCGACCTCACCTACTCATCTTAATGCTCACGAGGCCACCTCATCCTATTATAAGGGCGCCATCAGACATGTCCCTAAACGACCCGGTAAGATATACCTGGGTTAACCAGGGTCTCATTAACTAAAAGTTCCCTTGAGTAGATCCCTTGTGCGCAACTTATTTGAGAGCCTGATCGTGTTGCTGTCACGTCACTCTCTAGAAGTGTGGACGCAGTATTTAGGGTATCCTCCAATCCTCAACAACGTGGAGAGCCTGCGTATCCATCTTGACGAAGCCGGTAACGACTCCAAAGCCAGTAAGATTCCGCAAATCATATATCCAAGATGGCCACTGAGCTGGATTCAACCCTTCAAAAAACGCCTTTTCCGCCATTCGGTGGGGTCGACGTCGTACTCAAAACACAATCCACTAGACTGAGTGGGCATCCATGGGACCACAAGGTTTTTAATATGAGTCGTTTAGGGCTTTGCGTCTTACGAGTGTGTCAGGCACGATATTACGCGACACACTAAGGCAAAAGTGGGCGGTGAGTGTTCGGGGCCATCCAACGTGAGGGGGTTCACTCTAGCGCGAGATCTGAACAACTCTTCCAACTCGTTATGTTCTCAGTATACGGAGGGACGACCCTCAAGGGACAGCTTAAATAAGCATGTTCACTAGGGATAGGCTTAGTAAAGAAGTTACTGGTACGGTTCGCCGTCTGTCACCCAGGATGAGCAGGTACAGGCAGATGATCCATAGCGCCATCGGTACGATGATGTGCTCCGGACTTAGAGGTAGAGGTTTCTCTAAGACTCGGTACCGGGAAGAGCGAAGCACAACCCCCGCAACTCGAAGGTCATTGGGCAGATGGGTCCCCTAAGCGGTCTATAGTGTTACAGTATACGGCACGTGAATGCGTAGCACATGTCAAGGGTTGTGGCCTTCGGGGCGTGTAGACTTCTAGTTCTGATAAAGACCTCCTTTAACCTTTATACTGTGTGCAAAACACGCTGGCTTGTGCTGGGCGTATACCCCCAAGACGCCTCTCGAACTCCGTGGAAATCCGGCGACTTCCAGGACGAGAAGTTTGTTAGTGTAACAGCCCCATTGGATTGGTCCAAAGACCGACGGGTGACGTGTGCCGGCACGAGGGTTCCTTAATTTGTTGTAAGATACGTACCCCTCGGCGGAGGGACGCACGCACCACCCACACAAAGAAGTACGACAGGACAATACTATAATGCGTAGGCTAACCTTCAGTATTGCCCGGAGTGCGTTCAGGCCAAGTTGTCAGCCATTCTGGCTTAGTACCTCGTCTCTCACCTAGAGCCCACACGCCCTCAGCCAATTGGTGAGTCATTTTGATGGTACATCTTTGGCCGTGGAAGTGTCTGTTACACTCTCTACAGGAGGTTAGCGCCGATGAGTTGCAACCGTCTTACAATATTTCAATATCGCTAAGAAGCGGAACGTTGTGCAGCACGACGGCGCTAGGGACTATGAGCTACGGCCTAGGCGGTTGCCACTATAAGGGGGCGCGTTGGAAACCAACATCGCATCTCCGATCCCCATCCCGAAGACAATACGACTGGAAACCCCCGATTTCCTAATTACCGCCATTGCTTTTTACCCAAAGCTTCCAGGACGCCGTATGCGACAGCTAAGGCGTCGGGCCTTACACCACGTTGAGGCGGTGGGTTCTTGGGGAGGCGAGCAAGTTCCCGTTGTGTGACGCACCGACAAATTTGGTTAGGGTCCTGTTCGCAAAGATTAGCCGGATCAAGCAGATAGACGCCGGAGCATCAGTCAGTTGACAGTCTGTTACTGCCGTTTTGAAGAGAAAGGCCCTGCAAGAGGCGTGAGAGAACTTCTTTGTGCGAGGTACGCGGGTGCAATTCTGAGGGTAGTATCGACTTACGTGAATCTAGGAACCGAACCTGGCAAGCTGGTGACTATGACCTGTGGCTCGCACAATTAATCTCGGGAAAGAATTAAACGCCTCCTAGCCGACGGGATCAACTGGTAACGCAATTTTGCAAAATCCCATTTTGCGGACGGCTACCGACCAGATACTGGCCCATGGGTCGTTGACCGGCTCTCCCCCTCTACCACAAGAGCTTAAGACGCTCAGGAACGTACGGCGTCCAGAAGACTGCTAGCTTTAGATCACCCTGGACGGTGGAGTTTATTGGTCAACTTGTGTATTATGAAACGCCCTCATAGGCGGCGAGAGACCGTTAAGGTACACGTTTGTTATGTAGAGAGGGGAGGGGATTTAACTGGTGCAGTAAAGTTTTTGTACGAGGCGAGAGGCAATGTAAGTCATTCAAATTGCCTTTGGCCTATGTGGCTAGCTTGAACACCAAGGTAATATCCGTCATGTCGATGAGTTTCTGCACAGGCGATGTGTTGCGCAGGTTCCGTCTGGATGACCTGGTCTAGCACCGGCGATACGCGCCCGTTGGCTACTCCCGCTAGCTAGGTAATGGTTCCCTTGAACCGCGGCCAAGTACTAGTTCGGTCAATTATCGGACATCCTGAACATGACAAGCGTTCCTCCTGTCTACGAGAGTACCGCAGAGGTCGAACGGCGAGATGGATCCGATCTAAAGTAGAATCCCAGGGTTGCTTCAATTTCCGATCCCTAGATTACGGATGGGTGGTTAAATTTTCGGCATGATGAGGCGCCCAGTACTGTCCATAGAAGACTTGACCTTCCTCACAGGGTCTCCCGTACGTAAGTTTGAACTAATTAATCGCCAACGAAGAAGAAGAACACTATGATCGCGTGCATCGATCGCTCGTGGCGTTGCTGCGAGTGTTACAAGCCCACTGGGACAACTCGCTCAAGACGCGGCTGTAGGCCCGCTGTTGGCAACCTCTGACTCTACGGCTGTACCATCGAAGAACTATAATTTTATCACTACCATATCTACATAATCTTAACGCCCGCTTTTCGGTCCCTCAATGAAGTGAGGAGGAATGTCGCCCTACTGTGATGCACAGACATAGTTCCATCGATCGCCGACCTCCCATGCACAATACGTGTATCAGATGTATAGCCAGTGTTAAGTGTATAATTGGCGATATATCTGTGCACCATGCATCTGCGACAGCTTCTACTGCTCATGGCGGGTCATCGAGTAGATTCGTGTTCTCGCGGGGCAGTATATTTAAGTACCGTAACACGGCCGTTGAAAGCCCCATTCTTCTGAAGGGCTGCTCGTCGCTGTGTCGTTCTATTTGTCCCTCTCGGGAGCTTACGCCTTAACGATTTTTCTGTGTTATTACTAACTCGGCTGACTTGGAGGATCATTGTAATTAGAGATACGTACTAGCAGACCTACATTGTGAATACGCGGGCGAACTTCGTCGACCAGAACTACAGCCCTTCTCGATGCCATGTCCGATTCATGATTCCTGAGGAATGGGAACATAGATACTTGCAGGTTTCTACTATTCCCCGCAGCTGAGGCGATTTACGAATGCGAATCTCTGAACGGTATAAAGTTCGAAAATTGGCCCAATCGGCGGCGTGGCATCACGTTAAGGGTGTGTGCATCCCCGAAACATGGACGCGCCACCGTTCCGTAGAGGTGAGCCAGGCAGTATGCCTCCATACCGACGCGGCGTGTCGAACGGGCCGATTTACTTCGACCCGGGAGGTTAAAATCATAACAGGGGGGGAAAAGGGAGCGAGACTACTGCACACCAGTGTACGTTACATCTATGAGAGCGACGCGTACGGGCTAGCTCCTGAGAGGACGTTACTGACTACAGATCCATCCGCACGCATTCCGGAATGTAAGGAGGGTGAGTGACAAAACTGCCAGTACTGGCGCCGACTACAAACAAAAGACTTTCACTACCTCTTTCCAGACAGACAAGGCAGCTGGGCCAATACGCTCCTGGCCCGAGCTAGACACTCCTGCGCCGCCATGTGTTCATCACGCATAGTGACGTTGTAAGCAGCCCCGAAGTATCACACCCGAACTAGCTGCTGCAGATTTCTTGTTCGCTGTGCCCGCCATAGTATAATAGGTTATAACCATACTTCCCGTACTTTGGATTGTCTCATGGCGAGACTTATTGTGATACTAAACCCATACATCGGGTTTGTTTATCGGCGCGGGTCCAGGTGCACCGCTGCGTCGGCACTTATCGCCCTATGGTACCCTCGCGGCAAACTAGAGGGCCTACGGTGACAGTCGTGGCCGCTATTATTGCTTCTTGACCTCAACATGTCGCAGTGTGCCGTGCTCCCCCGCACATAACGCCGCTCTGATGCGGGACACGATATTCATATGTACTCGCTCAACGTAAGTCAGGCCGGACGCCGTAGTACTAGCAGCAGTAAACGGGGATTGTAGTGCCATCAACTAAACCTGCGCAGCTGCGCATTATTTATTGGGGTCCCTGCCCCGATTGTGGTGGTTTGAAGAACTAAGCGCAACGCTATTGAAACGTTGCAGACTTCCATTGTCGTGGGACATTGCCCACAAAAAAGGCGACAACGCTGCGCTTAGTACCAATCAAGCTCTCCGTGTCTAGTCGTTCGGTTAATCTCTACAAATTATTCAATCCGTTCCCTGCGCGAACGGAGCTAGCTTGGGGTTCGAGTATAAGACTACCTGTGTGGTGAGTACTCATGGTAGACGGCGCCAATTAGTCCGCGAGTCCGCATGGCAAGCGCGCGGAAGTGGATCGGCCAGGGGATTCGTGCACCATTAACTCCGCACAGCTGCTGTGGTTTACACACACAGGTGACTCGCTTTCGATTGATCACACGTCCAGGTTCGTCGTCAGGCCTTCCTCTAACCGTTTGTTTAAACTCTGCGTAACGCACCGAACATCCCGATTTAGCAAGGAAGTCCCCACGTATTTTAGTATGTGTCTCCGAAACTATAAGAAACAAAACCTCGGGGGACTAGCGCGTACGGACTGGGCCTTCAGCGGGTTAGGGTTACCTAATTTCGTATATGATTGCGGACGGAGACGACCTCCAGTGCTCTAAATCAGTGAGCTGGAGTGGTAGAATGAAGAAATGCACATACGGGATGTTGGCCACCAACAGGCGTACGCGATGAAGTACGATTCGGAAAAAAATGCTATGAAATGGTGCAGTGGGGAGCCAGTCGACCAGCTTTGGTGGACAGTCGCGGCTGCGGCCCGGAAGGGCAATATAGGATGCTATTTGGCTGAGCTCCATCCTACCTAGGGGCGTTACTCGTCGTACTTTTTGGAAAGTTCGAGAAGTGGGCGCGTCAGAGTGCGCCAGCGCGCGAAATTGGCTATTTGGCGGGTCTCGGTTGGATCTGGGTGACGCTATTAGGGCTAAATCTTCTTATGCTCTAATAGAAGAGGGGCCTTAGGCTGGCAGTTAGTCGACACTTTGACAATTCTGCCATGACCCAGTGGAACTTGTTTTAGTCTCTACGGAACACGCAAACGCAGCGCGAAACCTTGGGCCCCCCACACGAAGCCGTGATGACACTATAATTGTCCGCTTAGACCCCTGTCAGAACTCCACGCCTGCTTCTCGTACACATGTCTGCTAACGGGCTAACGCAGTCATAATGCCGCCTCACTCTGTGATATATCGTAAGTAAACGCGGTTCCTACGCAAT"
reverseComplement(pattern)

def patternMatching(pattern,genome):
    positions = []
    len_text=len(genome)
    len_pattern=len(pattern)
    for i in range(len_text-len_pattern+1):
        if genome[i:i+len_pattern] == pattern:
            positions.append(str(i))
    return ' '.join(positions)
    
pattern='CTTGATCAT'
genome= open("Vibrio_cholerae.txt").read()
patternMatching(pattern,genome)



def clumpFinding(genome,k,L,t):
    kmers = set()
    len_genome=len(genome)
    for i in range(len_genome-L+1):
        freqWords=frequentWords(genome[i:i+L],k)
        if list(freqWords.keys())[0]>=t:
            for val in freqWords.values():
                kmers.add(val[0])
    return kmers
    

genome=open('E_coli.txt').read()
k=9
L=500
t=3  
' '.join(clumpFinding(genome,k,L,t))


import itertools

def createDictionary(k):
    dic={}
    nucleotides = 'ACGT'
    for perm in itertools.product(nucleotides,repeat=k):
        dic[''.join(perm)]=0
    return dic

def patternToNumber(dic,kmer):
    #dic = createDictionary(len(pattern))
    return list(dic.keys()).index(kmer)

def numberToPattern(dic,index):
    return list(dic.items())[index][0]

"""
ComputingFrequencies(Text, k)
        for i ← 0 to 4k − 1
            FrequencyArray(i) ← 0
        for i ← 0 to |Text| − k
            Pattern ← Text(i, k)
            j ← PatternToNumber(Pattern)
            FrequencyArray(j) ← FrequencyArray(j) + 1
        return FrequencyArray
""" 

def computingFrequencies(text, k):
    frequencyArray=createDictionary(k)
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        #j=patternToNumber(frequencyArray,'GT')
        frequencyArray[pattern]=frequencyArray[pattern]+1
    return frequencyArray

' '.join([str(val)for val in computingFrequencies('TTGTTGACGCACACTGAGGCCATAGGTGAAACTTGTTGGATTAAAGCTCTTACGCCCTTGACCTCCCAGAGTCGATTGGAGCGGTCATCACCACCGTTTCTTCGGTGATTCATCACCACGGGTCAAATCTGGCGTTGATATAAGAACGGGCTTCACGTGTTAGGCCCTACCGTGGGTTTCTGTTGGAGTCACGGGAGCGCAACGTGTTGAGCACTAAACTCCAGTGTATAACCCTCGTCTTCTTATTCGCGCAGACTGCGGTATTATGTCTTAAGCATAATAGAGTGCTATTGAAAGGGCGCACCCAGAGTAACACCGATTATCCCGTCCTTATTCTTGAAATCCCTACTCGGAGTCAGGAGTGAGTGTTGATCGGGTTACAATAATCCTGGGAACTCGACGGGTAGTCCCGGTGGCCCGATTGGGCCAATTTTTTAGAAACTTCGTAGTTCAGTAATGCAGTACGACCCTTCTAATGCCTCGCCGGTCAGCAGCGGCCATACTTACGGAGTCAGACCCTCAGTTCCGACTAACATGACTTGAGAAACTCTCGGTAACCTTTTTCTCGTCTGTTGCGAAGGACTCTACACACATATACAGCTCATGGTCGAGGGTTGACGGGAGAT', 8).values()])

"""
 FasterFrequentWords(Text, k)
        FrequentPatterns ← an empty set
        FrequencyArray ← ComputingFrequencies(Text, k)
        maxCount ← maximal value in FrequencyArray
        for i ← 0 to 4k − 1
            if FrequencyArray(i) = maxCount
                Pattern ← NumberToPattern(i, k)
                add Pattern to the set FrequentPatterns
        return FrequentPatterns
"""  
 
def fasterFrequentWords(text,k):
    frequentPatterns = set()
    frequencyArray=computingFrequencies(text, k)
    max_count=max(frequencyArray.values())
    frequentPatterns = [pattern for pattern in frequencyArray if frequencyArray[pattern] == max_count]
    return {max_count:frequentPatterns}

"""
   PatternToNumber(Pattern)
        if Pattern contains no symbols
            return 0
        symbol ← LastSymbol(Pattern)
        Prefix ← Prefix(Pattern)
        return 4 · PatternToNumber(Prefix) + SymbolToNumber(symbol)
"""
def patternToNumberV2(pattern):
    if len(pattern) == 0:
        return 0
    symbol=pattern[-1:]
    prefix=pattern[:-1]
    return 4*patternToNumberV2(prefix)+symbolToNumber(symbol)

def symbolToNumber(symbol):
    nucleotides='ACGT'
    return nucleotides.find(symbol)

patternToNumberV2('ACGGCCTAGGGCCATATCGT')
 
pattern='12345'

pattern[1]

"""
NumberToPattern(index, k)
        if k = 1
            return NumberToSymbol(index)
        prefixIndex ← Quotient(index, 4)
        r ← Remainder(index, 4)
        symbol ← NumberToSymbol(r)
        PrefixPattern ← NumberToPattern(prefixIndex, k − 1)
        return concatenation of PrefixPattern with symbol
"""

def numberToSymbol(index):
    return 'ACGT'[index]

int(11/4)
11%4

def numberToPatternV2(index, k):
    if k == 1:
        return numberToSymbol(index)
    prefixIndex = int(index/ 4)
    r = index % 4
    symbol = numberToSymbol(r)
    prefixPattern = numberToPatternV2(prefixIndex, k-1)
    return prefixPattern + symbol

numberToPatternV2(6298,11)

"""
FindingFrequentWordsBySorting(Text , k)
        FrequentPatterns ← an empty set
        for i ← 0 to |Text| − k
            Pattern ← Text(i, k)
            Index(i) ← PatternToNumber(Pattern)
            Count(i) ← 1
        SortedIndex ← Sort(Index)
        for i ← 1 to |Text| − k
            if SortedIndex(i) = SortedIndex(i − 1)
                Count(i) = Count(i − 1) + 1
        maxCount ← maximum value in the array Count
        for i ← 0 to |Text| − k
            if Count(i) = maxCount
                Pattern ← NumberToPattern(SortedIndex(i), k)
                add Pattern to the set FrequentPatterns
        return FrequentPatterns
"""
"""
ClumpFinding(Genome, k, L, t)
        FrequentPatterns ← an empty set
        for i ← 0 to 4k − 1
            Clump(i) ← 0
        for i ← 0 to |Genome| − L
            Text ← the string of length L starting at position i in Genome 
            FrequencyArray ← ComputingFrequencies(Text, k)
            for index ← 0 to 4k − 1
                if FrequencyArray(index) ≥ t
                    Clump(index) ← 1
        for i ← 0 to 4k − 1
            if Clump(i) = 1
                Pattern ← NumberToPattern(i, k)
                add Pattern to the set FrequentPatterns
        return FrequentPatterns
"""
"""
BetterClumpFinding(Genome, k, t, L)
        FrequentPatterns ← an empty set
        for i ← 0 to 4k − 1
            Clump(i) ← 0
        Text ← Genome(0, L)
        FrequencyArray ← ComputingFrequencies(Text, k)
        for i ← 0 to 4k − 1
            if FrequencyArray(i) ≥ t
                Clump(i) ← 1
        for i ← 1 to |Genome| − L
            FirstPattern ← Genome(i − 1, k)
            index ← PatternToNumber(FirstPattern)
            FrequencyArray(index) ← FrequencyArray(index) − 1
            LastPattern ← Genome(i + L − k, k)
            index ← PatternToNumber(LastPattern)
            FrequencyArray(index) ← FrequencyArray(index) + 1
            if FrequencyArray(index) ≥ t
                Clump(index) ← 1
        for i ← 0 to 4k − 1
            if Clump(i) = 1
                Pattern ← NumberToPattern(i, k)
                add Pattern to the set FrequentPatterns
        return FrequentPatterns
"""