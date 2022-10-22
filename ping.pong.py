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
        if self.rect.x > 650 or self.rect.x < 0:
            self.speed_x *= -1
        if sprite.collide_rect(racket_1,ball) or sprite.collide_rect(racket_2,ball):
            self.speed_x *= -1
class MenuButton(sprite.Sprite):
    def __init__(self,photo,rect_x,rect_y,weight,height): 
        super().__init__()
        self.weight = weight
        self.height = height
        self.image = transform.scale(image.load(photo),(self.weight,self.height))
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)
    def show_buttons(self):
        play_button.reset()
        replay_button.reset()
        exit_button.reset()



racket_2 = Racket('rackk.png',650,0,5,50,150)
racket_1 = Racket('rackk.png',0,0,5,50,150)
ball = Ball('balls.png',100,100,2,50,40)
play_button = MenuButton('play.png',240,100,250,70)
replay_button = MenuButton('replay.png',240,220,250,70)
exit_button = MenuButton('exit.png',240,340,250,70)
team1 = 0
team2 = 0
clock = time.Clock()
FPS = 30
finish = True
game = True

font.init()
font2 = font.Font(None,72)
font1 = font.Font(None,36)
text_win1 = font2.render('PLAYER 1 WIN!',1,(255,215,0))
text_win2 = font2.render('PLAYER 2 WIN!',1,(255,215,0))

while game:
    
    for i in event.get():
        if i.type == QUIT:
            game = False
        if i.type == MOUSEBUTTONDOWN and i.button == 1:
            x,y = i.pos
            if play_button.collidepoint(x,y):
                finish = False
            if replay_button.collidepoint(x,y):
                ball.rect.x , ball.rect.y = 100,100
                racket_1.x , racket_1.y = 0, 0
                racket_2.x , racket_2.y = 650, 0
                finish = False
            if exit_button.collidepoint(x,y):
                game = False
        if i.type == KEYDOWN:
            if i.key == K_ESCAPE:
                if finish == True:
                    finish = False
                elif finish == False:
                    finish = True
            if i.key == K_r:
                ball.rect.x , ball.rect.y = 100,100
                racket_1.x , racket_1.y = 0, 0
                racket_2.x , racket_2.y = 650, 0
                finish = False
            if  i.key == K_SPACE:
                finish = False

    if finish != True:
        window.blit(background,(0,0))
        racket_1.update_l()
        racket_2.update_r()
        ball.update_ball()

        number2 = font1.render('points:'+str(team2),1,(0,0,0))
        number1 = font1.render('points:'+str(team1),1,(0,0,0))
        racket_1.reset()
        racket_2.reset()
        ball.reset()
        window.blit(number1,(40,50))
        window.blit(number2,(560,50))

        if ball.rect.x < 0:
            team2 += 1
        if ball.rect.x > 650:
            team1 += 1
        if team2 == 5:
            window.blit(text_win2,(200,50))
            finish = True   
        if team1 == 5:
            window.blit(text_win1,(200,50))
            finish = True
    else :

        play_button.reset()
        replay_button.reset()
        exit_button.reset()

    clock.tick(FPS)
    display.update()








