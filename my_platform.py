import play
import pygame
from random import randint

#                                          -ГГ-
Main_Hero = play.new_circle(color='black', x=-350, y=20, radius=10, border_color='black')
lava = play.new_box(color='red', x=0, y=-290, width=play.screen.width, height=20)
Main_Hero.current_color_number = 0
playing = True
#                                          -Text-
Guide = play.new_text(words='Press e to use next color', color='black', x=-275, y=290, size=60)
Guide2 = play.new_text(words='Press q to use past color', color='black', x=-275, y=270, size=60)
result_text = play.new_text(words="")
end = play.new_text(words="the end", x=-310, y=180)

active_colors = ["red", "blue"]


#                                     -circles with colors-
colored_circles = [
    play.new_circle(color='yellow', radius=21, x=-250, y=0),
    play.new_circle(color='green', radius=21, x=200, y=0),
    # play.new_circle(color='red', radius=21, x=150, y=0)
]
#                                       -lines with color-
colored_lines = [
    play.new_box(color='red', height=50, width=10, x=220, y=290),
    play.new_box(color='blue', height=50, width=10, x=230, y=290)
]

#                                        -Platforms-

plats=[
    play.new_box(x=-350, y=-250, width=80, height=10),
    play.new_box(x=-250, y=-270, width=80, height=10, color="red"),
    play.new_box(x=-150, y=-220, width=80, height=10, color="blue"),
    play.new_box(x=0, y=-150, width=80, height=10, color="red"),
    play.new_box(x=110, y=-80, width=80, height=10, color="yellow"),
    play.new_box(x=-180, y=-100, width=130, height=50, color="blue"),
    play.new_box(x=250, y=50, width=80, height=50, color="black"),
    play.new_box(x=-200, y=90, width=30, height=10, color="green"),
    play.new_box(x=-150, y=90, width=30, height=10, color="yellow"),
    play.new_box(x=75, y=90, width=30, height=10, color="yellow"),
    play.new_box(x=150, y=90, width=30, height=10, color="green"),
    play.new_box(x=20, y=100, width=30, height=10, color="black"),
    play.new_box(x=-170, y=90, width=30, height=10, color="blue"),
    play.new_box(x=-100, y=100, width=30, height=10, color="red"),
    play.new_box(x=-310, y=130, width=100, height=10, color="black"),

]




def get_color(sign="+"):
    cur_num = Main_Hero.current_color_number
    if sign == "+":
        cur_num += 1
    elif sign == "-":
        cur_num -= 1  
    else:
        return
    cur_num = cur_num % len(active_colors)
    Main_Hero.current_color_number = cur_num
    return active_colors[cur_num]

def hide_all_except_same_colored():
    for p in plats:
        try:
            if not p.is_hidden and p.color not in (Main_Hero.color, 'black'):
                p.stop_physics()
                p.hide()
            elif p.is_hidden and p.color in (Main_Hero.color, 'black'):
                p.show()
                p.start_physics(can_move=False)
        except KeyError:
            pass
    for line in colored_lines:
        if line.color == Main_Hero.color:
            line.border_width = 2
        else:
            line.border_width = 0

def play_while_playing(func):
    global playing
    async def wrapper():
        if playing:
            await func()
    return wrapper

#                                         -Physics-
Main_Hero.start_physics(bounciness=0.1)
for p in plats:
    p.start_physics(can_move=False)

@play.when_program_starts
@play_while_playing
async def start():
    hide_all_except_same_colored()

@play.repeat_forever
@play_while_playing
async def jump():
    for p in plats:
        if p.is_touching(Main_Hero) and play.key_is_pressed("w"):
            a = Main_Hero.physics.x_speed
            Main_Hero.physics.y_speed = 50
            Main_Hero.physics.x_speed = a
            #hide_all_except_same_colored()
#                                       -Color Changing-
@play.repeat_forever
@play_while_playing
async def rnk():
    if play.key_is_pressed("e"):

        Main_Hero.color = get_color(sign="+")
        hide_all_except_same_colored()
        await play.timer(seconds=0.2)
    elif play.key_is_pressed("q"):
        Main_Hero.color = get_color(sign="-")
        hide_all_except_same_colored()
        await play.timer(seconds=0.2)

@play.repeat_forever
@play_while_playing
async def move():
    if play.key_is_pressed("a"):
        Main_Hero.physics.x_speed = -10
    elif play.key_is_pressed("d"):
        Main_Hero.physics.x_speed = 10
    elif play.key_is_pressed("s"):
        Main_Hero.physics.x_speed = 0

@play.repeat_forever
@play_while_playing
async def collect_circle():
    for c in colored_circles:
        if Main_Hero.is_touching(c) and c.color not in active_colors:
            active_colors.append(c.color)
            c.hide()
            x_new_line = max([cir.x for cir in colored_lines]) + 10
            colored_lines.append(
                play.new_box(color=c.color, height=50, width=10, x=x_new_line, y=290)
            )

@play.repeat_forever
@play_while_playing
async def lose():
    global playing
    if Main_Hero.is_touching(lava):
        playing = False
        Guide.words = ""
        Guide2.words = ""
        result_text.words = "You lost"
        for p in plats:
            if p.physics:
                p.stop_physics()
            p.hide()
        for c in colored_circles:
            c.hide()
        for l in colored_lines:
            l.hide()
        Main_Hero.stop_physics()
        Main_Hero.hide()
        lava.hide()
        end.hide()
    elif Main_Hero.is_touching(end):
        playing = False
        Guide.words = ""
        Guide2.words = ""
        result_text.words = "You win"
        for p in plats:
            if p.physics:
                p.stop_physics()
            p.hide()
        for c in colored_circles:
            c.hide()
        for l in colored_lines:
            l.hide()
        Main_Hero.stop_physics()
        Main_Hero.hide()
        lava.hide()
        end.hide()
play.start_program()