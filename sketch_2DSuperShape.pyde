n1=0.8
n2=0.3
n3=1.3
m=190
a=1
b=1

def superFactor(angle):
    p1 = pow(abs((1 / a) * cos(angle * m / 4)),n2)
    p2 = pow(abs((1 / b) * sin(angle * m / 4)),n3)
    p3 = pow(p1+p2,1/n1)
    return 1/p3

def keyPressed():
    global m
    if key == CODED:
        if keyCode == UP:
            m+=1
        elif keyCode == DOWN:
            m-=1
def setup():
    size(400,400)
    
def draw():
    translate(width/2,height/2)
    background(51)
    numPoints = 1000
    inc = (2*PI)/numPoints
    angle=0
    stroke(255)
    noFill()
    beginShape()
    for i in range(numPoints):
        x = 100 * superFactor(angle) * cos(angle)
        y = 100 * superFactor(angle) * sin(angle)
        angle+=inc
        vertex(x,y)
    endShape(CLOSE)
    
