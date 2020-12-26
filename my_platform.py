import play
import pygame
from random import randint

play.set_backdrop('light green')
platform = play.new_box(color="black",width=20,height=120)
platform.start_physics(bounciness=0)

text = play.new_text(words='Tap W,A,S,D to move', x=0, y=play.screen.bottom+60, size=70)
line1=play.new_box(color="blue",width=800,height=20,x=0,y=-290)
line1.start_physics(can_move=False)
line2=play.new_box(color="blue",width=800,height=20,x=0,y=290)
line2.start_physics(can_move=False)
line3=play.new_box(color="blue",width=20,height=640,x=390,y=0)
line3.start_physics(can_move=False)
line4=play.new_box(color="blue",width=20,height=640,x=-390,y=0)
line4.start_physics(can_move=False)
finish = play.new_circle(color="red",size=30,x=20,y=-190,angle=90)

level_boxes = [
    play.new_box(color="blue",width=15,height=160,x=-60,y=-180),
    play.new_box(color="blue",width=15,height=160,x=100,y=-180),
    play.new_box(color="blue",width=15,height=160,x=20,y=-100,angle=90)
]
for level_box in level_boxes:
    level_box.start_physics(can_move=False)

level = 1

def clear_level():
    for level_box in level_boxes:
        level_box.stop_physics()
        level_box.hide()
    level_boxes.clear()

async def next_level():
    global level
    
    level += 1
    if level == 2:
        clear_level()
        create_level2()
    elif level == 3:
        clear_level()
        create_level3()
    elif level == 4:
        clear_level()
        create_level4()

def create_level2():
    global level_boxes
    new_boxes = [
        play.new_box(color="blue",width=15,height=160,x=-60,y=-220),
        play.new_box(color="blue",width=15,height=160,x=100,y=-220),
        play.new_box(color="blue",width=15,height=160,x=-60,y=-60),
        play.new_box(color="blue",width=15,height=160,x=100,y=-60),
        play.new_box(color="blue",width=15,height=160,x=100,y=100),
        play.new_box(color="blue",width=15,height=160,x=20,y=180,angle=90),
        play.new_box(color="blue",width=15,height=160,x=-90,y=80),
        play.new_box(color="blue",width=30,height=20,x=-75,y=10),
        play.new_box(color="blue",width=15,height=70,x=-52,y=220),
        play.new_box(color="blue",width=15,height=300,x=-240,y=152,angle=90)
    ]
    for box in new_boxes:
        box.start_physics(can_move=False)

    level_boxes += new_boxes

    finish.x = 260
    finish.y = -220

def create_level3():
    global level_boxes
    new_boxes = [
        play.new_box(color="grey",width=15,height=160,x=-60,y=-220),
        play.new_box(color="grey",width=15,height=160,x=100,y=-220),
        play.new_box(color="grey",width=15,height=160,x=-60,y=-60),
        play.new_box(color="grey",width=15,height=160,x=100,y=-60),
        play.new_box(color="grey",width=15,height=160,x=100,y=100),
        play.new_box(color="grey",width=15,height=160,x=20,y=180,angle=90),
        play.new_box(color="grey",width=15,height=170,x=-90,y=90),
        play.new_box(color="grey",width=15,height=70,x=-52,y=220),
        play.new_box(color="grey",width=15,height=290,x=-200,y=180,angle=90)       
    ]
    play.set_backdrop('dimgrey')
    text.words = "ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR"
    text.color = "red"
    for box in new_boxes:
        box.start_physics(can_move=False)
    level_boxes += new_boxes
    finish.x = 10
    finish.y = -220
    finish.color = "white"

def create_level4():
    global level_boxes
    play.set_backdrop('purple')
    text.words = "Congratulation, you complete the game"
    text.color = "gold"
    finish.x = 0
    finish.y = 0
    finish.color = "purple"


    
#level2_objects = [lv2box1, lv2box2 ,lv2box3, lv2box4,]
@play.repeat_forever
async def game():
    if play.key_is_pressed('a'):
        platform.physics.x_speed = -20
        platform.physics.y_speed = 0
    elif play.key_is_pressed('d'):
        platform.physics.x_speed = 20
        platform.physics.y_speed = 0
    elif play.key_is_pressed('s'):
        platform.physics.y_speed = -20    
    elif play.key_is_pressed('w'):
        platform.physics.y_speed = 20
    else:
        platform.physics.x_speed=0
        platform.physics.y_speed=0

@play.repeat_forever
def cheats():
    if play.key_is_pressed('C'):
        cheat = play.new_text(words="Che4t_Me^u",x=0,y=200)
        cheat2 = play.new_text(words="Pre$$ Q,E t0 us3",x=0,y=160,size=60)
    if play.key_is_pressed('B'):
        pass
    if play.key_is_pressed('N'):
        pass

@play.repeat_forever
async def check_next_level():
    if platform.is_touching(finish):
        await next_level()




play.start_program()