# -*- coding: utf-8 -*-
"""
Created on Wed May 22 23:16:05 2019

@author: s140121038
"""

import matplotlib.pyplot as plt  
import numpy as np
import itertools 
import xlrd

#import coordinate.csv
def coordinates():
    
    A = np.genfromtxt('Coordinates.csv' , dtype ='str',
                      delimiter=',', encoding='utf-8').T
    name = A[0]
    y = A[1].astype(float)
    x = A[2].astype(float)
   
    fig, ax = plt.subplots(figsize=(10,5))
    plt.plot(x,y,'.')
    return name, x,y
#import distancematrix.csv
def distances():
    
    workbook = xlrd.open_workbook('distancematrix.xls')  
	  
    worksheet = workbook.sheet_by_name('Sayfa1')  
    
    dislist = []  
	  
    for i,j in itertools.product(range(81),range(81)):  
	           
	        elements = worksheet.cell_value(i+3,j+2)  
	        dislist.append(elements)  
	          
    elements=np.arange(0,7000,81)  
	  
    for i in range(81):
    
	    dislist[elements[i]+i]=0       
	  
    dismatrix=np.reshape(dislist,(81,81))  
#    print(dismatrix)
    return dismatrix

def get_path(n):
    start=np.where(name=='Ankara')
    l = list(range(n))
    l=np.delete(l,start)
    np.random.shuffle(l)
    l= np.insert(l,0,start)  
    return l

def get_path_length(path): #it is calculating from coordinates
    path = np.append(path,path[0])
    total_length = 0.0
    for i in range(len(path)-1):
        j = path[i]
        k = path[i+1]
        dist = np.sqrt((x[j]-x[k])*2+(y[j]-y[k])*2)

        total_length = total_length+dist  
    return total_length

def path_length(path):  #it is calculating from distancesmatrix
    dist=distances()
    def distance(i,j):
        return dist[i][j]
    total_length=0
    for i,j in zip(path[:-1],path[1:]):
        d=distance(i,j)
        total_length=total_length+d
    return total_length

def draw_path(path):
    path = np.append(path,path[0])
    
    plt.plot(x[path],y[path],'-o')
  
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
name,x,y=coordinates()
dist=distances()
fig, ax =plt.subplots(figsize=((45-26),(42-36)))
plt.plot(y,x,'-o')
plt.show()
n=len(x)
n_population=100

l=get_path(n)
print('Any route length starting from Ankara is =',path_length(l))

draw_path(l)
plt.show()
population, fitness  = create_initial_population(n_population,n)

for i in range(10000):
  print('Number of iteration=',i+1)
  population, fitness=next_generation(population)
  print('The shortest length =',fitness.min(),'\nThe average length =',
        fitness.mean())
  best_path = population[0]
  draw_path(best_path)
  plt.show()
  plt.plot(fitness)
  plt.show()











