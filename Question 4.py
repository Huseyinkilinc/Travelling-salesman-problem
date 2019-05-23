# -*- coding: utf-8 -*-
"""
Created on Thu May 23 03:45:33 2019

@author: s140121038
"""

 
def cross_over(gene1,gene2):
    
  r = np.random.randint(len(gene1)) # cross over location
  newgene = np.append(gene1[:r],gene2[r:]) # may be a defunct gene
    
  missing = set(gene1)-set(newgene)
  elements, count = np.unique(newgene, return_counts=True)
  duplicates = elements[count==2]
  duplicate_indices=(newgene[:, None] == duplicates).argmax(axis=0)
  
  newgene[duplicate_indices]=list(missing) # now proper.
  
  if np.random.rand()<0.5:
    i1,i2 = np.random.randint(0,len(newgene),2)
    newgene[[i1,i2]] = newgene[[i2,i1]] 
  return newgene

def create_initial_population(m,n):
    population = []
    fitness = []
    for i in range(m):
        gene = get_path(n)
        path_length1 = path_length(gene)
        
        population.append(gene)
        fitness.append(path_length1)
  
    population = np.array(population)
    fitness = np.array(fitness)  
    sortedindex = np.argsort(fitness)
    return population[sortedindex], fitness[sortedindex]

def next_generation(population):
    pop = []
    fit = []
    i=0
    f=int(np.sqrt(len(population)))
    for gene1 in population[:f]:
        for gene2 in population[:f]:
            i=i+1      
            x =  cross_over(gene1,gene2)
            l = path_length(x)
            pop.append(x)
            fit.append(l)
  
    population = np.array(pop)
    fitness = np.array(fit)  
    sortedindex = np.argsort(fitness)
    return population[sortedindex], fitness[sortedindex]