import play
import pygame
from random import randint
image = play.new_image(image='cave.jpeg', size=310)

text = play.new_text(words='0', color='lime', y=175)

rocks = []

t = play.new_text(words='r = retry, a = left, d = right', y=120)
#pl_b = play.new_box(color='cyan', width=3000, height=1000)
ice = play.new_image(image='ice.png', size=25, x=-300, y=0)
ice.start_physics(bounciness=2.5, stable=True)
txt = play.new_text(words='', color='maroon', size=125, x=-160, y=60)
monster = play.new_box(color='cyan', width=50, height=100, x=0, y=10)
monster.start_physics(can_move=False)

pl1 = play.new_box(color='cyan', height=15, width=50, x = -300, y=-200)
pl2 = play.new_box(color='cyan', height=15, width=50, x = -200, y=-200)
pl3 = play.new_box(color='blue', height=15, width=60, x = 0, y=-100)
pl4 = play.new_box(color='cyan', height=15, width=50, x = 150, y=-200)
pl6 = play.new_box(color='blue', height=300, width=100, x = 350, y=-250)

pl1.start_physics(can_move=False)
pl2.start_physics(can_move=False)
pl3.start_physics(can_move=False)
pl4.start_physics(can_move=False)
pl6.start_physics(can_move=False)

@play.repeat_forever
def move():
    ice.physics.x_speed = 0
    if play.key_is_pressed('left'):
        ice.physics.x_speed = -20
    if play.key_is_pressed('right'):
        ice.physics.x_speed = 20
    if play.key_is_pressed('r'):
        ice.x = -300
        ice.y = 50
        txt.words = ''

@play.repeat_forever
async def fall():
    rock = play.new_circle(color='grey', x=randint(-300,300), y = 255, radius=20)
    rock.start_physics()
    rocks.append(rock)
    await play.timer(1.5)

@play.repeat_forever
def doo():
    for rock in rocks:
        if rock.y <= -245:
            rocks.remove(rock)
            rock.remove()
        if rock.is_touching(ice):
            bad_end()

def bad_end():
    txt.words = 'YOU DIED'
    ice.x = -300
    ice.y = 50
    text.words = '0'

@play.repeat_forever
def do():
    if ice.y <= -220: 
        bad_end()

@play.repeat_forever
def end():
    if ice.x >= 300:
        ice.x = -300
        ice.y = 50
        txt.words = ''
        text.words = str(int(text.words) + 1)

#потом зделать чтоб падали камни с помощью hide и show!!! спасибо, будующий Миша)

play.start_program()