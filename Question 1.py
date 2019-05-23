# -*- coding: utf-8 -*-
"""
Created on Thu May 23 03:42:43 2019

@author: s140121038
"""

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
