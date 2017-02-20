#solution to problem BA1E in rosalind's textbook track set find the k-mers/"words" forming clumps in a DNA sequence

#this is the first problem that requires building on previous problems in the textbook track series

#the imput is a DNA string, and integers k(length of k-mer), L(genome interval for clump), t(minimum repeats in clump)

#first import the data
def input_load():
 #get string from file
 f = input("Please input file with sequence/s of interest: ")

 #open file, read contents
 start = open(f, "r")
 newfile = start.read()
	
 #split file into seq entries
 stringlist = []
 seqno = newfile.count("\n")
 stringlist = newfile.split("\n")
 stringlist.remove('')

 #find the inputs and the dna
 dna = stringlist[0]
 implist = stringlist[1].split(" ")

 #find integer input parameters
 k = int(implist[0])
 L = int(implist[1])
 t = int(implist[2])
		
 return dna, k, L, t

#now we need to use the approach from the slider problem (ba1a), except we need to nested slider functions, one to get L islands and an inner one to count pattern matches

#here are two functions from the k-mer count problem (ba1b)
def dnaread(dna, k):
 i = 0
 kmers = []
 while i < (len(dna) - k):
  kmers.append(dna[i:i+k])
  i += 1
 return kmers

#use a fxn to find multiple counts of various kmers, (python's Statistics module 'mode' function doesn't work with multimodal data)
def clumps(array):
    count = list(map(array.count, array))
    return list(set(filter(lambda x: array.count(x) >= t, array)))

#sliding function, which identifies and counts matches
def island(dna, k, L, t):

 clumpat = []
 i = 0

 while i < (len(dna)-L):
  #define the island of dna to be assessed
  seq = dna[i:i+L]
  
  #now define various patterns and find
  kmers = dnaread(seq, k)

  #filter kmer list for threshold
  clump = clumps(kmers)

  #add unique elements of each new clump to final list
  for el in clump:
   clumpat.append(el)

  #this will iterate over all k-mers in the island, reset the counters, move to next island
  i += 1
  
 return clumpat

dna, k, L, t = input_load()
patterns = island(dna, k, L, t)

for word in set(patterns):
 print(word, end=' ')





