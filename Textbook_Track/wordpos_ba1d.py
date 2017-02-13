#solution to problem BA1C in rosalind's textbook track set find the position of a given k-mer/"word" in a DNA sequence

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

 #find the k-mer and the dna
 word = stringlist[0]
 dna = stringlist[1]

 #find k-mer length
 k = len(stringlist[0])
		
 return word, dna, k

#function to find and store k-mer positions in a list
def posfind(dna, word, k):
 i = 0
 posse = []
 while i < (len(dna) - k):
  if dna[i:i+k] == word:
   posse.append(i)
   i += 1
  else:
   i += 1
 return posse

#run fxns
word, dna, k = pattern_load()
poslist = posfind(dna, word, k)

for no in poslist:
 print(no, end=' ')
