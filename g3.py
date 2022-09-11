import pgzrun
HEIGHT=500
WIDTH=500

a1=Actor('character_0000',pos=(50,100)) 
a2= Actor('character_0019',pos=(20,20))
a3=Actor('character_0020',pos=(100,30))
a4=Actor('character_0022',pos=(200,300))
a5=Actor('character_0004',pos=(300,300))
a6=Actor('character_0024',pos=(400,500))



def draw():
    screen.fill('blue')
    a1.draw()
    a2.draw()
    a3.draw()
    a4.draw()
    a5.draw()
    a5.draw()
    a6.draw()
    


def update():
    a2.x +=1
    if a2.x >HEIGHT:
     a2.x=0

     a5.y += 80
    if a5.y >HEIGHT:
     a5.y=0

pgzrun.go()