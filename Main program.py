# -*- coding: utf-8 -*-
"""
Created on Thu May 23 03:46:18 2019

@author: s140121038
"""

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

for i in range(100):
  print('Number of iteration=',i+1)
  population, fitness=next_generation(population)
  print('The shortest length =',fitness.min(),'\nThe average length =',
        fitness.mean())
  best_path = population[0]
  draw_path(best_path)
  plt.show()
  plt.plot(fitness)
  plt.show()
