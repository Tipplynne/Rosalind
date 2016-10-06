"""This script calculates numbers of mortal rabbits in a population using dynamic programming to implement a recurrence relation as part of the Rosalind Bioinformatics Stronghold problem set FIBD

Ive essentially just modified the code from the FIB (rrr.py) problem
"""

#First get input values n and m.
n = int(input("Please input generation number n: "))

m = int(input("Please input life expectancy, in months: "))

#The problem does not stipulate the numbers of pairs produced so I'm assuming one pair generated per adult pair
k = 1

#create recursive function breed, which takes integers from the sample dataset, i.e. generations, fecundity and life expectany (mortality)

def breed(gen, juv, mort):
    
#this first step is the base case, because a recursive function, or, a function that calls itself needs some way to stop. The first month there is only one pair of bunnies (juvenile), so state that
 if gen == 1:
  return 1
  
#the number of pairs in month 2 is still 1 (the first juvenile pair matures), the number of pairs in month 3 is = that in month 1 plus the juvies produced in month 2
 elif gen == 2:
  return juv
    
#now our function continues to call itself until it hits on of the base cases  
 f1 = breed(gen-1, juv, mort)
 f2 = breed(gen-2, juv, mort)
 
#from month 3, up to month "mort" and if gen = mort, population size is predicted by adding previous two generations, i.e. we only need to call the function once to get to the base cases
  
 if gen <= mort: 
  print('sanity')
  return (f1+(f2*juv))
 
#However if we have a generation time greater than life expectancy, we need to modify f1 and f2 to reflect the population "mort" months previously. Not really sure how this works (but it does!), and thinking recursively about how modified f1 and f2 actually go back to the f1 and f2 of the original function really hurts my brain (hence the commented out 'sanity' print statements). This is crazy though. The time-step doubles with every generation, it takes too long to solve within the rosalind's 5min time limit. 1m14s to solve a 37gen, 20mort case. It needs to be able to solve a 100min20mort case in 5mins. How to speed this up? 
 elif gen > mort:
  print('insanity')
  #f1 = breed(gen-mort+1, juv, mort)
  #f2 = breed(gen-mort, juv, mort)
  
#a different approach. both approaches are actually failing hard =(  
  mortality = breed(gen-mort, juv, mort) 
  return f1+(f2*juv) - mortality
  
print(breed(n,k,m))
     
 


	
