from random import randint
import numpy as np
from functools import reduce

######################################

def solver_python(grid):
    num = np.arange(1,10)
    m,j = np.where(grid == 0)
    if ( m.size == 0 ):
        return(True,grid)
    else:
        m = m[0]
        j = j[0]    
        Row = grid[m,:] 
        Col = grid[:,j]
        Sqr = grid[(m // 3) * 3: ( 3 + ( m // 3 ) * 3 ),( j // 3 ) * 3:( 3 + ( j // 3 )* 3 ) ].reshape(9)
        Value = np.setdiff1d(num , reduce(np.union1d,(Row,Col,Sqr)))
        grid_temp = np.copy(grid) 
        for value in Value:
            grid_temp[m,j] = value
            tt = solver_python(grid_temp)
            if (tt[0]):
                return(tt)
        return(False,None)
    
########################################
    
t = np.array([[0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0]])

t[randint(0 , 9)][randint(0 , 9)] = randint(0 , 9)
t = solver_python(t)[1]

##########################################

x = int(input(" Number Delete: "))

for m in range (x):
    t[randint(0 , 9)][randint(0 , 9)] = 0
    
##########-----PRINT-----##################
    
print (t)
