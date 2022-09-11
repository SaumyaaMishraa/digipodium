import pgzrun
from random import randint

HEIGHT=500
WIDTH=500
score=0
player= Actor('character_0001', pos=(50,50))
item=Actor('character_0021', pos=(100,100))
speed =3


def draw():
    screen.fill('black')
    player.draw()
    item.draw()
     screen.draw.text(f'SCORE: {score}', topleft=(10,500-30),color='white')
     music.play("powfu")

def update():
    global score  #global variable

    #movement control
    if keyboard.left:
        player.x -= speed
    if keyboard.right:
        player.x += speed
    if keyboard.down:
        player.y += speed
    if keyboard.up:
        player.y -= speed

# boundary control
        if player.x> WIDTH:
            player.x =0
        if player.x < 0:
            player.x = WIDTH
        if player.y> HEIGHT:
            player.y =0
        if player.y < 0:
            player.y = HEIGHT

#collision control
        if player.colliderect(item):
         score +=1
        item.x= randint(0,WIDTH)
        item.y=randint(0,HEIGHT)
        sounds.sound1.play()

pgzrun.go()