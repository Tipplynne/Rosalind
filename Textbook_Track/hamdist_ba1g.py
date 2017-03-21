#solution to problem BA1G in rosalind's textbook track set to calculate the hamming distance (no. of mismatches) between two sequences, p and q, usually denoted HammingDistance(p,q)

#create function
def HammingDistance(p,q):
 return(sum(b1!=b2 for b1,b2 in zip(p,q)))

#Get the sequences
with open('rosalind_ba1g.txt', 'r') as inputfile:
 p = inputfile.readline().strip()
 q = inputfile.readline().strip()

print(HammingDistance(p,q))

#Note: can also use biopython's pairwise2.align.global function, which may be more applicable to later problems, but here is just overkill
