# This script calculates numbers of rabbits in a population using dynamic programming to implement a recurrence relation as part of the Rosalind Bioinformatics Stronghold problem set

#First get input values n and k.
n = int(input("Please input generation number n: "))

k = int(input("Please input pairs generated at each reproduction event: "))

#create a loop to calculate recursively

F1 = 1
F2 = 1
F=1
n= n-2
i=0
while i < n:

	F2 = F*k #the problem here is coding the delay, the new bunnies need some time to mature
	print(F2)

	F = F2 + F1
	print(F)

	F1 = F
	print(F1)

	i += 1
	print(i)


print(F)
	


	
