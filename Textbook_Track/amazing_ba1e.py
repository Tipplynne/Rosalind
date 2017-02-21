#NOT MINE, but an amazingly short solution to problem BA1E in rosalind's textbook track set find the k-mers/"words" forming clumps in a DNA sequence submitted by user "Sedictious"

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

#The sedictious effect:


def find_clumps(strings,k,L,t):
 substrings = []

 for i in range(len(strings)-k-1):
  substrings.append(strings[i:i+k])

 for i in list(set(substrings)):
  temp = 0
  j = 0

  while j<= (len(strings)-L-1):
   f = strings[j:j+L].count(i)

   if f>=t:
    print(i,end=" ")
    break

   j+=(t-f-1)*k+1


dna, k, L, t = input_load()
find_clumps(dna, k, L, t)

