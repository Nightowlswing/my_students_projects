import play
import pygame
from random import randint

win = False
lose = False
tet = play.new_image(image ="r.png", size = 200)
dog = play.new_image(image = "j.jpg", size = 5, x = -300, y = -230)
het = []
platform = play.new_box(color = "lime", x = -300, y = -250, width = 200, height = 10)
badplatform = play.new_box(color = "green", x = randint(-250,250), y = -60, width = 200, height = 10)
loseplatform = play.new_box(color = "green", x = 100, y = -300, width = 1000, height = 10)
yet = play.new_box(color = "yellow", x = randint(-250,250), y = -150, width = 200, height = 10)
get = play.new_box(color = "cyan", x = randint(-250,250), y = -20, width = 200, height = 10)
uet = play.new_box(color = "bisque", x = randint(-250,250), y = 40, width = 200, height = 10)
ret = play.new_box(color = "black", x = randint(-250,250), y = 120, width = 200, height = 10)
fat = play.new_image(image= "t.png", x = -100, y = 250, size = 10)
het.append(platform)
het.append(yet)
het.append(get)
het.append(uet)
het.append(ret)
het.append(fat)
play.set_backdrop("whitesmoke")
dog.start_physics()
platform.start_physics(obeys_gravity=False, stable=True)
loseplatform.start_physics(obeys_gravity=False, stable=True)
yet.start_physics(obeys_gravity=False, stable=True)
get.start_physics(obeys_gravity=False, stable=True)
uet.start_physics(obeys_gravity=False, stable=True)
@play.repeat_forever
def do():
    if play.key_is_pressed("left"):
        dog.physics.x_speed = -30
    elif play.key_is_pressed("right"):
        dog.physics.x_speed = 30
    # elif play.key_is_pressed("up"):
    #     dog.physics.y_speed = 5
    # elif play.key_is_pressed("down"):
    #     dog.physics.y_speed = -10 
    else:
        dog.physics.x_speed = 0

@play.repeat_forever
def up():
    for h in het:
        if play.key_is_pressed("up") and h.is_touching(dog):
            dog.physics.y_speed = 50


@play.repeat_forever
def let():
    global lose
    if dog.is_touching(loseplatform) and not lose:
        lose = True
        text = play.new_text(words="YOU LOSE!!!", color = 'red')
        dog.remove()

@play.repeat_forever
def ket():
    global win
    if dog.is_touching(fat) and not win:
        win = True
        text = play.new_text(words="YOU WIN!!!", color = 'lime')
        dog.remove()

@play.repeat_forever
async def sat():
    for i in het:
        if dog.is_touching(i):
            await play.timer(1)
            i.stop_physics()
            i.start_physics()



play.start_program()


#тут подключи нужны звуки. Например, звук сбора монетки

#счетчик монет
#score_txt = play.new_text(words='Score:', x=play.screen.right-100, y=play.screen.top-30, size=70)
#score = play.new_text(words='0', x=play.screen.right-30, y=play.screen.top-30, size=70)

#подсказки
#text = play.new_text(words='Tap SPACE to jump, LEFT/RIGHT to move', x=0, y=play.screen.bottom+60, size=70)

#sea = play.new_box(
        #color='blue', width=play.screen.width, height=50, x=0, y=play.screen.bottom+20
    #)

#def draw_platforms():
    #добавь сюда платформы, по которым будет перемещаться персонаж
    #pass

#def draw_coins():
    #добавь сюда монетки, которык будет собирать персонаж
    #pass

#@play.when_program_starts
#def start():
    #подключи фоновую музыку

    #draw_platforms()
    #draw_coins()

#@play.repeat_forever
#async def game():
    #тут опиши процесс игры
    #await play.timer(seconds=1/48)

