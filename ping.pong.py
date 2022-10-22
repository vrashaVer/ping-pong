from pygame import *

window = display.set_mode((700,500))
background = transform.scale(image.load('background.jpg'),(700,500))
display.set_caption('Пінг Понг')

class GameSprite(sprite.Sprite):

    def __init__(self,photo,rect_x,rect_y,speed,weight,height):
        super().__init__()
        self.weight = weight
        self.height = height
        self.image = transform.scale(image.load(photo),(self.weight,self.height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Racket(GameSprite):
    def update_l(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 350:
            self.rect.y += self.speed
    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed
class Ball(GameSprite):

    def __init__(self,photo,rect_x,rect_y,speed,weight,height):
        super().__init__(photo,rect_x,rect_y,speed,weight,height)
        self.speed_x = 5
        self.speed_y = 5

    def update_ball(self):
    
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.y > 450 or self.rect.y < 0:
            self.speed_y *= -1
        if sprite.collide_rect(racket_1,ball) or sprite.collide_rect(racket_2,ball):
            self.speed_x *= -1




racket_2 = Racket('rackk.png',650,0,5,50,150)
racket_1 = Racket('rackk.png',0,0,5,50,150)
ball = Ball('balls.png',100,100,2,50,40)


clock = time.Clock()
FPS = 30
finish = False
game = True

font.init()
font2 = font.Font(None,72)
text_win1 = font2.render('PLAYER 1 WIN!',1,(255,215,0))
text_win2 = font2.render('PLAYER 2 WIN!',1,(255,215,0))
while game:
    
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        racket_1.update_l()
        racket_2.update_r()
        ball.update_ball()


        racket_1.reset()
        racket_2.reset()
        ball.reset()

        if ball.rect.x < 0:
           window.blit(text_win2,(200,200))
        if ball.rect.x > 650:
            window.blit(text_win1,(200,200))


    clock.tick(FPS)
    display.update()








