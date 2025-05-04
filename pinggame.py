from pygame import *
window = display.set_mode((700, 500)) # создаем окно приложения
display.set_caption('ping pong') # заголовок окна
BACK = (200, 255, 255)# фон с цветом
window.fill(BACK)

game = True
finish = False
clock = time.Clock()
fps = 120

while game:
    for e in event.get(): # для всех событий системы
        if e.type == QUIT: # если событие типа нажатие на крестик
                game = False # завершаем
    if finish != True:
        window.fill(BACK)







    display.update()
    clock.tick(fps)
