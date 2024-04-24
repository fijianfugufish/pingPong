from pygame import *
from math import sqrt, pow
from random import randint

winx,winy = 700,500
padding = 5

game = True

window = display.set_mode((winx,winy))
display.set_caption('pingPong')
background = transform.scale(image.load('black.png'),(700,500))

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

class ball(gameSprite):
    def __init__(self,sprite,X,Y,w,h,speed): 
        super().__init__(sprite,X,Y,w,h,speed)
        self.Xv = speed
        self.Yv = speed
    def move(self):
        self.rect.y -= self.Yv
        self.rect.x -= self.Xv
    def yodoiyoingyeah(self):
        if self.checkCollision(paddle1):
            self.speed += 0.25
            self.Xv = self.speed * -1
            self.Yv = randint((self.speed * -1)//1,(self.speed)//1)
        elif self.checkCollision(paddle2):
            self.speed += 0.25
            self.Xv = self.speed 
            self.Yv = randint((self.speed * -1)//1,(self.speed)//1)
        if self.rect.y <= 0:
            self.Yv = self.speed * -1
        elif self.rect.y >= 500 - self.w:
            self.Yv = self.speed
        if self.rect.x <= -100:
            global game
            game = False
        elif self.rect.x >= 800 - self.w:
            game = False

paddle1 = player('paddleTexture.jpg',5,20,10,100,5,True)
paddle2 = player('paddleTexture.jpg',685,20,10,100,5,False)

ball = ball('ball.png',350,250,50,50,2.5)

clock = time.Clock()
FPS = 60

eelbruv = False

while game:
    window.blit(background,(0,0))
    paddle1.blit()
    paddle2.blit()
    ball.blit()
    
    paddle1.move()
    paddle2.move()
    ball.move()

    ball.yodoiyoingyeah()

    display.update()

    for e in event.get():
        if e.type == QUIT:
            eelbruv = True
            break

    if eelbruv:
        break    
    
    clock.tick(FPS)

lost = gameSprite('lost.png',0,0,700,500,0)
lost.blit()

while not game:
    for e in event.get():
        if e.type == QUIT:
            game = True

    clock.tick(FPS)

    display.update()
