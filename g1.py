from ctypes import alignment
import pgzrun 

WIDTH= 500
HEIGHT= 500

def draw():
    screen.fill('white')
    screen.draw.text('HELLO PYGAME', (WIDTH//2,HEIGHT//2) ,color='red' ,fontsize=30)screen.draw.text('Example 0ne', (WIDTH//2,HEIGHT//2) ,color='red' ,fontsize=30)



pgzrun.go()