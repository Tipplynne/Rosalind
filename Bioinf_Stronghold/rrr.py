# This script calculates numbers of rabbits in a population using dynamic programming to implement a recurrence relation as part of the Rosalind Bioinformatics Stronghold problem set

#First get input values n and k.
n = int(input("Please input generation number n: "))

k = int(input("Please input pairs generated at each reproduction event: "))

#create a loop to calculate recursively

F1 = 1
F2 = 1
for i in n:
	F = F2 + F1
	F2 = F1*k #bug here
	F1 = F - F2
	i += 1

print(F)
	


	
