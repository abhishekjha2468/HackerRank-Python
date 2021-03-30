import math
import os
import random
import re
import sys
def unique(list1): 
    unique_list = [] 
    for x in list1: 
        if x not in unique_list: 
            unique_list.append(x) 
    return unique_list


if __name__ == '__main__':
    s = input()
    list = list(s)
    a = unique(list)
    b = []
    for i in a:
        b.append(s.count(i))
    
    if len(a)>2:
    	p=0
    	f=0
    	while a!=[]:
    		max = 0
   	 	for i in range(0,len(b)): 
   	 		if b[i] > max: max = b[i]
  	  	z = []
  	  	for i in range(0,b.count(max)):
    			index1 = b.index(max)
    			z.append(str(str(a[index1])+" "+str(b[index1])))
    			a.pop(index1)
    			b.pop(index1)
    		z.sort()
    		for i in z:
    			if p<3:
    				print(i)
    			else:
    				f=1
    				break
    			p=p+1
    		if f==1:
    			break