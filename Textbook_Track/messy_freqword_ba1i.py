#this is a solution to Project Rosalind's BA1I problem, which uses the HammingDistance function to find the most frequent words/patterns of length k (above a certain mismatch threshold, d) within a larger string of text


#function to find and store k-mer positions in a list, mod from ba1d
def messy_posfind(dna, pattern, k, d):
 i = 0
 posse = [pattern]
 while i <= (len(dna) - k):
  if (HammingDistance(dna[i:i+k], pattern)) <= d:
   posse.append(dna[i:i+k])
   i += 1
  else:
   i += 1
 print(posse)
 return set(posse)

#function to split the DNA into k-mers, 
def dnaread(dna, k):
 i = 0
 kmers = []
 while i <= (len(dna) - k):
  kmers.append(dna[i:i+k])
  i += 1
 return set(kmers)

#Hd function
def HammingDistance(p,q):
 return(sum(b1!=b2 for b1,b2 in zip(p,q)))

#use a fxn to find multiple modes
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

#get functions from other file to list the mutants of all kmers
from assistant import *

#open list of matched mismatches
occurance = []
mutant_kmers = []

#for each of the possible kmers:
for kmer in kmers:
 #create all possible variants, with number of mutations representing d
 mutant_kmers = d_cons(kmer, d)
 occurance.append(kmer)
 #for each variant, check whether there are hits, with minimum number of mismatches
 for mu in mutant_kmers:
  temp = messy_posfind(dna, mu, k, d)
  #this is just extra formatting so I dont get lists within lists
  for el in temp:
   occurance.append(el)
print(occurance)

max_kmers = mode(occurance)

for word in max_kmers:
 print(word, end=' ')
 

