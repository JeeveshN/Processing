ANGLE = PI/4
def mouseWheel(event):
    global ANGLE
    if event.getCount() == 1:
        ANGLE+=0.1
    else:
        ANGLE-=0.1
    
def setup():
    size(500,500)
    
def draw():
    background(51)
    translate(width/2,height)
    branch(130)   
    
def branch(length):
    stroke(255)
    line(0,0,0,-length)
    translate(0,-length)
    if length > 5 :
        pushMatrix()
        rotate(ANGLE)
        branch(length*0.7)
        popMatrix()
        pushMatrix()
        rotate(-ANGLE)
        branch(length*0.7)
        popMatrix()
