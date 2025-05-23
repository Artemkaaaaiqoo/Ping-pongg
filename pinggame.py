from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_img, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_img), (size_x, size_y))
        self.speed = player_speed
        # прямоугольник каждого спрайта
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self): # перемещение для левой
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 200:
            self.rect.y += self.speed
    def update_r(self): # перемещение для правой
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - 200:
            self.rect.y += self.speed
window = display.set_mode((700, 500)) # создаем окно приложения
display.set_caption('ping pong') # заголовок окна
BACK = (200, 255, 255)# фон с цветом
window.fill(BACK)

game = True
finish = False
clock = time.Clock()
fps = 120

player_r = Player('rocket.png', 620, 200, 5, 50, 200)
player_l = Player('rocket.png', 30, 200, 5, 50, 200)

ball = GameSprite('ball.png', 200, 200, 5 ,50, 50)

speed_x = ball.speed
speed_y = ball.speed

font.init()
font = font.Font(None, 35)
win_r = font.render('Правый игрок победил', True, (0, 255, 0))
win_l = font.render('Левый игрок победил', True, (0, 255, 0))



while game:
    for e in event.get(): # для всех событий системы
        if e.type == QUIT: # если событие типа нажатие на крестик
                game = False # завершаем
    if finish != True:
        window.fill(BACK)
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        player_r.update_r()
        player_l.update_l()
        
        if ball.rect.y > 500 - 50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(player_l, ball) or sprite.collide_rect(player_r, ball):
            speed_x *= -1

        if ball.rect.x < 0: # левая граница - проигрывает левый
            window.blit(win_r,(200, 200))
            finish = True
        if ball.rect.x > 700: # правая граница - проигрывает правый
            window.blit(win_l,(200, 200))
            finish = True



    player_r.reset()
    player_l.reset()
    ball.reset()

    





    display.update()
    clock.tick(fps)
