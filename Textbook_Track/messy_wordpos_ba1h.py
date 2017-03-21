#solution to problem BA1H in rosalind's textbook track set to find all approximate patterns in a genome string. I.e find all occurances (start positions) of a given pattern, above some mismatch threshold, d. For this, need to integrate the solutions from ba1d and ba1g: return start positions where HammingDistance(Genome, Pattern) ≤ d.

#sukkeling to get the import module funtions to work, need to figure out why, cos this copy-paste is getting to be a hack :(

#function to find Hd, from ba1h 
def HammingDistance(p,q):
 return(sum(b1!=b2 for b1,b2 in zip(p,q)))

#function to find and store k-mer positions in a list, mod from ba1d
def messy_posfind(dna, pattern, k, d):
 i = 0
 posse = []
 while i <= (len(dna) - k):
  if (HammingDistance(dna[i:i+k], pattern)) <= d:
   posse.append(i)
   i += 1
  else:
   i += 1
 return posse

#Get the input data
with open('rosalind_ba1h.txt', 'r') as inputfile:
 pattern = inputfile.readline().strip()
 dna = inputfile.readline().strip()
 k = len(pattern)
 d = int(inputfile.readline().strip())

poslist = messy_posfind(dna, pattern, k, d)

for no in poslist:
 print(no, end=' ')
