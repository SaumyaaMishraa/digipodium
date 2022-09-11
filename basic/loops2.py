from turtle import *
speed ('fastest')
color =['red','blue', 'green','pink', 'black', 'yellow']
pensize (4)
pencolor('black')
for i in range( 100,0,-1 ):
    pencolor(color[i%6])
    forward(100)
    left(360/6)
    circle(60)
    dot(i*2)


mainloop()

