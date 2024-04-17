from pygame import *
from math import sqrt, pow
from random import randint

winx,winy = 700,700
padding = 5

window = display.set_mode((winx,winy))
display.set_caption('pingPong')

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
    def __init__(self,sprite,X,Y,w,h,speed): 
        super().__init__(sprite,X,Y,w,h,speed)
        self.cd = 10
    def move(self):
        keysPressed = key.get_pressed()
        if keysPressed[K_w] and self.rect.y > (0 + self.w) + padding:
            self.rect.y += self.speed
        elif keysPressed[K_s] and self.rect.y > (winy - padding):
            self.rect.y -= self.speed

clock = time.Clock()
FPS = 60

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(FPS)

    display.update()

