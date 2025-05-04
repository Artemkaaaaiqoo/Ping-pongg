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

while game:
    for e in event.get(): # для всех событий системы
        if e.type == QUIT: # если событие типа нажатие на крестик
                game = False # завершаем
    if finish != True:
        window.fill(BACK)


    player_r.reset()
    player_l.reset()

    player_r.update_r()
    player_l.update_l()







    display.update()
    clock.tick(fps)
