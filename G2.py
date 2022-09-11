import pgzrun
from pygame import Rect

WIDTH= 500
HEIGHT= 500

box1 = Rect((50,50),(50,50))
box2 = Rect((100,100),(100,100))
def draw():
     screen.fill('white')
     screen .draw.rect(box1,'red')
     screen .draw.rect(box2,'blue')

def update():
        box1.x += 1
        if box1.x > WIDTH:
            box1.x=0

            box2.x -=1
        if box2.x <0:
         box2.x= WIDTH
    
        if box2.colliderect(box1):
          print('collision')
        box2.x += 4
     

pgzrun.go()