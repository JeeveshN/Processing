from random import randint
SCALE = 20
w=2000
h=2500
TERRAIN = [[randint(-10,10) for x in range(h/SCALE)] for y in range(w/SCALE)]
flySpeed=0

def setup():
    size(600,600,P3D)
    
def draw():
    global flySpeed
    flySpeed-=0.2
    yo=flySpeed
    for y in range(h/SCALE):
        xo=0
        for x in range(w/SCALE):
            TERRAIN[x][y] = map(noise(xo,yo),0,1,-100,100)
            xo+=0.2
        yo+=0.2
    background(0)
    stroke(255)
    noFill()
    translate(width/2,height/2)
    rotateX(PI/3)
    translate(-w/2,-h/2-200)
    col = w/SCALE
    row = h/SCALE
    
    for y in range(row-1):
        beginShape(TRIANGLE_STRIP)
        for x in range(col):
            vertex(x*SCALE,y*SCALE,TERRAIN[x][y])
            vertex(x*SCALE,(y+1)*SCALE,TERRAIN[x][y+1])
        endShape()
