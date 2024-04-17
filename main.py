from pygame import *
from math import sqrt, pow
from random import randint

winx,winy = 700,500
padding = 5

window = display.set_mode((winx,winy))
display.set_caption('pingPong')
background = transform.scale(image.load('blue.png'),(700,500))

font.init()
style = font.Font(None,36)

class gameSprite(sprite.Sprite):
    def __init__(self,sprite,X,Y,w,h,speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite),(w,h))
        self.w = w
        self.h = h
        self.speed = speed
        self.diagonalSpeed = ((sqrt((pow(speed,2) + pow(speed,2))) / 2) + speed / 7)
        self.rect = self.image.get_rect()
        self.rect.x = X
        self.rect.y = Y
    def blit(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    def checkCollision(self,obj):
        return Rect.colliderect(self.rect, obj.rect)

class player(gameSprite):
    def __init__(self,sprite,X,Y,w,h,speed,left): 
        super().__init__(sprite,X,Y,w,h,speed)
        self.left = left
    def move(self):
        keysPressed = key.get_pressed()
        if self.left:
            if keysPressed[K_w] and self.rect.y > (0) + padding:
                self.rect.y -= self.speed
            elif keysPressed[K_s] and self.rect.y < (winy - self.h - padding):
                self.rect.y += self.speed
        else:
            if keysPressed[K_UP] and self.rect.y > (0) + padding:
                self.rect.y -= self.speed
            elif keysPressed[K_DOWN] and self.rect.y < (winy - self.h - padding):
                self.rect.y += self.speed

paddle1 = player('paddleTexture.jpg',5,20,10,100,5,True)

clock = time.Clock()
FPS = 60

game = True
while game:
    window.blit(background,(0,0))
    paddle1.blit()
    
    paddle1.move()
    
    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(FPS)

    display.update()

