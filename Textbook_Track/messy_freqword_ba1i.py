#this is a solution to Project Rosalind's BA1I problem, which uses the HammingDistance function to find the most frequent words/patterns of length k (above a certain mismatch threshold, d) within a larger string of text

#over all workflow:
# 1) split dna string in list of overlapping kmers
# 2) for each kmer (pattern/word) find a list of varaints that differ from the original by, at max, d (mutations/mismatches) place all these variants into a set (called 'final' below)
# 3) use the hamming distance calculator determine how often each of these variants score a hit in the original sequence, everytime there is a hit add the variant to the 'count' list
# 4) find the variants that represent the modes of count and output to command line

from assistant import *

#function to split the DNA into k-mers

def dnaread(dna, k):
 i = 0
 kmers = [] 
 while i <= (len(dna) - k):
  kmers.append(dna[i:i+k])
  i += 1
 #print(kmers)
 return set(kmers)

#Hd function
def HammingDistance(p,q):
 return(sum(b1!=b2 for b1,b2 in zip(p,q)))

from itertools import combinations,product

#function to get all mutants(mismatch variants), from stack: http://stackoverflow.com/a/19890945/7800823
def mismatch(word, i = 2):
 for d in range(i+1):
  for locs in combinations(range(len(word)), d):
   thisWord = [[char] for char in word]
   for loc in locs:
    origChar = word[loc]
    thisWord[loc] = [l for l in "ACGT" if l != origChar]
   for poss in product(*thisWord):
    yield "".join(poss)    

#function to find and store k-mer positions in a list, mod from ba1d
def messy_posfind(dna, pattern, k, d):
 i = 0
 hits = 0
 while i <= (len(dna) - k):
  if (HammingDistance(dna[i:i+k], pattern)) <= d:
   hits += 1
   i += 1
  else:
   i += 1

 return (hits, pattern)

#use a fxn to find multiple modes, this step seems to take the most time, I hate using lamda fxns but stack overflow don't think there is any faster way to write a 'mode' function

def mode(array):
    most = max(list(map(array.count, array)))
    return list(set(filter(lambda x: array.count(x) == most, array)))


#Get the input data
with open('rosalind_ba1i.txt', 'r') as inputfile:
 dna = inputfile.readline().strip()
 inps = inputfile.readline().strip().split(" ")
 k, d = int(inps[0]), int(inps[1])


#first get list of all the occuring kmers, of k size
kmers = dnaread(dna, k)

#open list of matched mismatches
mutant_kmers = []
all_kmers = []

#for each of the possible kmers:
#######
tic()
#Most amount of time
for kmer in kmers:
 #create all possible variants, with number of mutations representing d
 mutant_kmers = list(mismatch(kmer, d))
 #this step just so I don't get lists within list
 for e in mutant_kmers:
  all_kmers.append(e)
toc()
#########

temp = []
counts = []

final = set(all_kmers)
tic()
from heapq import heappushpop, heappop, nlargest, heappush
for fin in final:
 heappush(counts, (messy_posfind(dna, fin, k, d)))
toc()


print(nlargest(4, counts, key=lambda x: x[0]))


