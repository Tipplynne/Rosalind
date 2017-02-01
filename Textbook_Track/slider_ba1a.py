# this is my approach to solving Rosalind's Textbook track problem BA1A

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
			
 return stringlist[0], stringlist[1]

#sliding function, which identifies and counts matches
def slide(seq, pat):

 its = 0
 i = 0
 while i < (len(seq)):
  if seq[i:i+len(pat)] == pat:
   its += 1
   i += 1
  else:
   i += 1

 return its

#run functions, out put no of matches
sequence, pattern = pattern_load()
iterations = slide(sequence, pattern)
print(iterations)
