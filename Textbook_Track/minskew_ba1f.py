#solution to problem BA1F in rosalind's textbook track set find the position in a genome minimizing the "skew" of a DNA string Genome, denoted Skew(Genome), which is the difference between the total number of occurrences of 'G' and 'C' in Genome


def minskewpos(genome):
 #first set variables to 0
 c = 0
 g = 0
 minskew = 0
 index = 0
 poslist = []
 for i in genome: 
  index += 1
  if i == 'C':
    c += 1
  if i == 'G':
    g += 1
  #calculate current skew
  skew = g-c
  #i.e. if a new minimum, reset the poslist
  if skew < minskew:
   poslist = [index]
   minskew = skew
  if skew == minskew and index not in poslist:
   poslist.append(index)
  
 return poslist

with open('rosalind_ba1f.txt', 'r') as inputfile:
 sequence = inputfile.readline()

for pos in minskewpos(sequence):
 print(pos, end=' ')
 
