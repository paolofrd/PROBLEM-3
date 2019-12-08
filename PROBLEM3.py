import ast
import math
import numpy as np
import sys

arr = input('Input an array: ')
arr = np.asarray(ast.literal_eval(arr))#convert string to list, convert list to array

lenarr = len(arr) #length of array
y = arr[0:lenarr,0] #locate y
x = arr[0:lenarr,1] #locate x

#storage
p1 = []
p2 = []
err = []

#function to compute for approximation
def comp():
    for n in range(1,lenarr):
        if lenarr <= 10:
            
            p1.append(np.polyfit(x,y,n)) #polynomial to vector, vector to array
            
            p2.append(np.polyval(np.polyfit(x,y,n),x)) #evaluate polynomial from vector, then is added to array
            fn = np.poly1d(np.polyval(np.polyfit(x,y,n),x))
            
            norm = np.linalg.norm(y-(np.polyval(np.polyfit(x,y,n),x)))
            normerr = np.min(norm)
        elif lenarr > 10:
            sys.exit('Program is limited to up to 10th degree only. Try again.')
    print('Coefficients within the polynomial function: \n',(np.polyval(np.polyfit(x,y,n),x)),'\n')
    print('Polynomail function: \n',fn,'\n')
    print('The least-norm error vector e(x): \n',normerr)
comp()