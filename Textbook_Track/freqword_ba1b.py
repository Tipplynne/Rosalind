#solution to problem BA1B in rosalind's textbook track set find the most frequent k-mer/"word" in a DNA sequence

#first import the data
def pattern_load():
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

 #find k-mer length
 k = int(stringlist[1])
		
 return stringlist[0], k

#function to split the DNA into k-mers
def dnaread(dna, k):
 i = 0
 kmers = []
 while i < (len(dna) - k):
  kmers.append(dna[i:i+k])
  i += 1
 return kmers

#use a fxn to find multiple modes, (python's Statistics module 'mode' function doesn't work with multimodal data)
def mode(array):
    most = max(list(map(array.count, array)))
    return list(set(filter(lambda x: array.count(x) == most, array)))

#run fxns
dna, k = pattern_load()
kmers = dnaread(dna, k)
modes = mode(kmers)

for word in modes:
 print(word, end=' ')


