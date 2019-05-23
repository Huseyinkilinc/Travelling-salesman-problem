# -*- coding: utf-8 -*-
"""
Created on Thu May 23 03:43:13 2019

@author: s140121038
"""

def get_path(n):
    start=np.where(name=='Ankara')
    l = list(range(n))
    l=np.delete(l,start)
    np.random.shuffle(l)
    l= np.insert(l,0,start)  
    return l
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