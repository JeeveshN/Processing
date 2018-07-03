from random import randint
from itertools import combinations
size_g=50
nu =0
def array(col,row):
    return [[randint(0,1) for i in range(col)] for j in range(row)]

GRID = array(size_g,size_g)
    
def compute_next_gen():
    global GRID
    ng = array(size_g,size_g)
    changes = list(set(list(combinations([-1,0,1,-1,1,0],2))))
    changes.remove((0,0))
    for i in range(size_g):
        for j in range(size_g):
            num=0
            for c in changes:
                x = i+c[0]
                y = j+c[1]
                try:
                    if GRID[x][y]==1 and x>=0 and y>=0:
                        num+=1
                except:
                    pass
            if num == 3:
                ng[i][j] = 1
            elif num<2 or num>3:
                ng[i][j] = 0
            else:
                ng[i][j]=GRID[i][j]
    GRID=ng

def mousePressed():
    width_r=width/size_g
    height_r=height/size_g
    GRID[int(mouseY/width_r)][int(mouseX/height_r)] = 1
        
def setup():
    size(1000,1000)
    
def draw():
    global nu
    start_x=0
    start_y=0
    width_r = width/size_g
    height_r = height/size_g
    stroke(0)
    for i in range(size_g):
        for j in range(size_g):
            if GRID[i][j] == 1:
                num=0
            else:
                num=255
            fill(num)
            rect(start_x,start_y,width_r,height_r)
            start_x+=width_r
        start_x=0
        start_y+=height_r
    if keyPressed:
        nu =1
    if nu ==1:
        compute_next_gen()
        

                
