from turtle import*
speed('fastest')
pencolor('black')
penup()
bgcolor('#76EEC6')
val=1
while True:
    forward (1*val)
    pendown()
    left(360/10)
 
    circle(8,70)
    val += 1