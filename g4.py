import pgzrun

HEIGHT=500
WIDTH=500

A1= Actor('character_0016', topleft=(50,50))

B2=Actor('character_0021', topleft=(100,100))
speed =3
def draw():
    screen.fill('black')
    A1.draw()
    B2.draw()

def update():
    A1.x +=1
    if A1.x > WIDTH:
        A1.x =0
    if keyboard.left:
        B2.x -= speed
    if keyboard.right:
        B2.x += speed
    if keyboard.up:
        B2.y += speed
    if keyboard.down:
        B2.y -= speed
    if B2.colliderect(A1):
        sounds.sound2.play()
    
pgzrun.go()