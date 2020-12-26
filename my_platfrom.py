import play
import pygame
from random import randint

play.set_backdrop('dimgray')


player = play.new_circle(color = "red", radius = 15, x = -350, y = 0, border_color = "black", border_width= 3)
#player.lvl = 1
Level = play.new_text(words = "Level 1", x = -320, y = 250)
name = play.new_text(words = "Чтоб перейти на второй", x = 0, y = 250)
name = play.new_text(words = "уровень, доберись до края экрана", x = 0, y = 220)

rocks = []

walls = [
    play.new_box(color = "black", width = 100, height = 300, x = -380, y = -250), 
    play.new_box(color = "black", width = 200, height = 300, x = -120, y = -250), 
    play.new_box(color = "black", width = 100, height = 300, x = 380, y = -250), 
    play.new_box(color = "black", width = 60, height = 20, x = 150, y = -50), 
    play.new_box(color = (15, 0, 0), width = 20, height = 143, x = 150, y = -130)
]

enemies = [
    play.new_box(color = "darkred", width = 110, height = 300, x = -275, y = -350),
    play.new_box(color = "darkred", width = 350, height = 300, x = 155, y = -350)
]

for platform in walls:
    platform.start_physics(can_move = False)

player.start_physics(bounciness=0.2)
player.can_jum = True

# enemies.append(e1)
# enemies.append(e2)

def clear_screen():
    global walls
    global enemies
    for e in enemies:
        #enemies.remove(e)
        e.remove()
    enemies.clear()
    for wall in walls:
        wall.stop_physics()
        wall.hide()
    walls.clear()
    for r in rocks:
        r.stop_physics()
        r.hide()
    rocks.clear()

@play.repeat_forever
async def jump():
    if player.can_jum:
        if play.key_is_pressed('w'):
            player.physics.y_speed = 70
            player.can_jum = False
    else:
        await play.timer(seconds=1.5)
        player.can_jum = True

@play.repeat_forever
def do():
    if play.key_is_pressed('a') or play.key_is_pressed('ф'):
        player.physics.x_speed = -15
    if play.key_is_pressed('d') or play.key_is_pressed('в'):
        player.physics.x_speed = 15

@play.repeat_forever
def enemy():
    for e1 in enemies:
        if player.is_touching(e1):
            player.x = -350
            player.y = 0
#######################################

#######################################

async def create_level2():
    global walls
    global enemies
    rocks.append(
        play.new_circle(color = "gray", radius = 80, x = 80, y = 20, border_color = "black", border_width= 5) 
    )
    rocks[0].start_physics(can_move = True, bounciness = 0)
    new_walls = [
        play.new_box(color = "black", width = 300, height = 300, x = 70, y = -250),
        play.new_box(x=390, y=50, width=20, height=300),
        play.new_box(color = "black", width = 100, height = 300, x = -380, y = -250)
    ]
    enemies.append(play.new_box(color = "darkred", width = 800, height = 300, x = 0, y = -350))
    

    for w in new_walls:
        w.start_physics(can_move=False)
    player.x = -350
    player.y = 0

    walls += new_walls
    await play.timer(0.01)

@play.repeat_forever
async def next_level():
    if player.x >= 370:
        clear_screen()
        number = int(Level.words[-1])
        number += 1
        if number == 2:
            await create_level2()
        elif number == 3:
            clear_screen()
            player.x = 0
            player.y = 0
            await play.timer(1)
            play.new_text(words="FINISH")
        Level.words = "Level " + str(number)
@play.repeat_forever
def end():
    if player.x >= 370 and int(Level.words[-1]) == 2:
        clear_screen()
        player.x = 0
        player.y = 0

play.start_program()