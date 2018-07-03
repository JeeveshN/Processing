from random import uniform


STARS = []
NUM = 1500

class Star:
    def __init__(self,h,w):
        self.x = uniform(-w,w)
        self.y = uniform(-h,h)
        self.z = random(w)
        self.px = self.x 
        self.py = self.y
        
    def show(self):
        speedx = map(self.x/self.z,0,1,0,width)
        speedy = map(self.y/self.z,0,1,0,height)
        size_e = map(self.z,width,0,0,8)
        stroke(255)
        if self.z!=width:
            line(self.px,self.py,speedx,speedy)
        ellipse(speedx,speedy,size_e,size_e)
        self.px = speedx
        self.py = speedy
        
    def update(self):
        self.z-=30
        if self.z < 1:
            self.z=width
            self.x = uniform(-width,width)
            self.y = uniform(-height,height)
    
def setup():
    global STARS
    size(800,800)
    background(0)
    STARS = [Star(height,width) for x in range(NUM)]
    
    
def draw():
    translate(height/2,width/2)
    background(0)
    for star in STARS:
        star.update()
        star.show()
    
    
