#This is code, taken from another coding project of mine, needs to be modified and used to create the library of all possible, single, double and triple replacement mutants for each kmer in the problem solution ba1i

#pattern constraints k <= 12, d <= 3

import pandas as pd
import regex as re

def single_mutants(wt, key):

 #Read in the sequence and send to a dataframe
 table = []
 table.append(list(wt))
 df = pd.DataFrame(table)
 mut_colno = len(wt) 

 #prepare a list of available bases
 bases = ['A', 'C', 'G', 'T']
 altbase = []

 #set the mutant seq number counter
 seq = 0
 counter = 0

 #iterate through the base list, until we hit a match with bases of the wildtype sequence (df columns)
 for base in bases:
  for pos in df.columns:

   #create regext of current position, to search mutation info, preventing back-mutations)
   pattern = r'{}'.format(pos+1)
   matchObj = re.search(pattern, key)

   #so if the base matches the wildtype and the position of previous mutation has not been covered
   if base == df.ix[0,pos] and matchObj == None:
    
    #prepare a list of alternate bases and use those to start new corresponding mutant seqs
    altbase.extend(bases)
    altbase.remove(base)
    df.set_value(seq+1, pos, altbase.pop())
    df.set_value(seq+2, pos, altbase.pop())
    df.set_value(seq+3, pos, altbase.pop())

    #summarise mutation info to new column, provided the mutants have not been seen before
    df.set_value(seq+1, mut_colno, '{}{}{}, {}'.format(base,pos+1,df.ix[seq+1,pos],key))
    df.set_value(seq+2, mut_colno, '{}{}{}, {}'.format(base,pos+1,df.ix[seq+2,pos],key))
    df.set_value(seq+3, mut_colno, '{}{}{}, {}'.format(base,pos+1,df.ix[seq+3,pos],key))
    seq += 3
 
 #replace the rest of the dataframe (empty mutant seq bases) with wildtype bases
 df = df.fillna(df.ix[0,df.columns])
 
 
 #change the column name for the mutations
 df = df.rename(columns = {mut_colno: 'Mutation'})

 #drop the wild type and rows where no mutation info was set, i.e where the same mutation has already happened
 df = df[df.Mutation.notnull()]
 
 return df.reset_index(drop = True)


def library_maker(df):
 #call the single mutants function and transpose the df, in order to count right (i.e., along the index)
 dft = df.T
 shape = len(df.columns) #to get column index, which is the mutation info, which will be used to create the keys
 mutant_dictionary = {}
 
 #put sequences in the library for the double replacement mutant library
 for mu in dft:
  mutant_dictionary.update({df.ix[mu,(shape-1)] : df.ix[mu,0:(shape-1)].str.cat()})
 
 return mutant_dictionary


def double_mutants(library):
 
#essentially what we're doing here is looping through the single mutant library, calling the single_mutant function again on each single_mutant to make the double mutants (this will naturally create duplicates). serially append each sub df to make double mutant df, then drop duplicates.
 ddf = pd.DataFrame()
 shape = len(ddf.columns)

 for key, seq in library.items():
  ddf = ddf.append(single_mutants(seq, key), ignore_index = True)
 
 return ddf.drop_duplicates(ddf.columns[0:(shape-1)], keep = 'last').reset_index(drop = True)

def triple_mutants(library):
 
#essentially what we're doing here is looping through the double mutant library, calling the single_mutant function again on each double_mutant to make the triple mutants (this will naturally create duplicates). serially append each sub df to make triple mutant df, then drop duplicates.
 ddf = pd.DataFrame()
 shape = len(ddf.columns)

 for key, seq in library.items():
  ddf = ddf.append(single_mutants(seq, key), ignore_index = True)
 
 return ddf.drop_duplicates(ddf.columns[0:(shape-1)], keep = 'last').reset_index(drop = True)

def d_cons(wt, d):
 
 kmers = []

 if d == 3:
  kmers.append(wt)
  df = single_mutants(wt, '')
  shape = len(df.columns)
  for i in range(shape):
   kmers.append(df.ix[i,0:(shape-1)].str.cat().upper())
  
  lib2 = library_maker(df)

  df = double_mutants(lib2)
  shape = len(df.columns)
  for i in range(shape):
   kmers.append(df.ix[i,0:(shape-1)].str.cat().upper())

  lib3 = library_maker(df)

  df = triple_mutants(lib3)
  shape = len(df.columns)
  for i in range(shape):
   kmers.append(df.ix[i,0:(shape-1)].str.cat().upper())

 elif d == 2:
  kmers.append(wt)
  df = single_mutants(wt, '')
  shape = len(df.columns)
  for i in range(shape):
   kmers.append(df.ix[i,0:(shape-1)].str.cat().upper())
  
  lib2 = library_maker(df)

  df = double_mutants(lib2)
  shape = len(df.columns)
  for i in range(shape):
   kmers.append(df.ix[i,0:(shape-1)].str.cat().upper())

 elif d == 1:
  kmers.append(wt)
  df = single_mutants(wt, '')
  dft = df.T
  shape = len(df.columns)
  print(shape)

  for i in dft:
   kmers.append(df.ix[i,0:(shape-1)].str.cat().upper())
  
 print(kmers)
 return set(kmers)

                
