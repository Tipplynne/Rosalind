# This script calculates numbers of rabbits in a population using dynamic programming to implement a recurrence relation as part of the Rosalind Bioinformatics Stronghold problem set RRR

#First get input values n and k.
n = int(input("Please input generation number n: "))

k = int(input("Please input pairs generated at each reproduction event: "))

#because my math education is lacking, for this problem I resorted to use a walk-through written in C+, published here: https://medium.com/algorithms-for-life/rosalind-walkthrough-rabbits-and-recurrence-relations-4812c0c2ddb3#.lqlh9d2go

#create recursive function breed, which takes two integers from the sample dataset, i.e. generations and number of baby rabbit pairs per reproductive event

def breed(gen, juv):

#this first step is the base case, because a recursive function, or, a function that cals itself needs some way to stop. The first month there is only one pair of bunnies (juvenile), so state that
 if gen == 1:
  return 1
  
#the number of pairs in month 2 is still 1 (the first juvenile pair matures), the number of pairs in month 3 is = that in month 1 plus the juvies produced in month 2
 elif gen == 2:
  return juv
  
#now our function continues to call itself until it hits on of the base cases  
 f1 = breed(gen-1, juv)
 f2 = breed(gen-2, juv)

#up to month 4, population size is predicted by adding previous two generations, i.e. we only need to call the function once to get to the base cases
 if gen <= 4:
  return f1+f2
  
#but this falls apart at month 5, i.e. the function hasn't got to either of the base cases by calling itself once. It needs to call itself recursively until it satisfies the base cases. The way I understand it is that the following line of code calculates backwards, calling itself everytime the base cases are not met. It's possible to check this with a printed counter beep. And would you know? this thing does not beep like fibonacci; but instead like fibonacci +1: with sequential increase in generation time from 5 onward: 1 2 4 7 12 20 33.
 
 else:
  #print("beep")
  return (f1+(f2*juv))
  
print breed(n,k)
     
 


	
