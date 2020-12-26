import play
import pygame
from random import randint
enemys=[]
bullets=[]
shields = []
play.set_backdrop('light green')
lose = False
win = False
pause = False

should_count_lose_count = True

#тут подключи нужны звуки. Например, звук сбора монетки
chudik=play.new_circle(color="red",radius=15,y=-150)
chudik.lose_count = 0
chudik.win_count = 0
#счетчик монет
#score_txt = play.new_text(words='Score:', x=play.screen.right-100, y=play.screen.top-30, size=70)
score = play.new_text(words='0', x=play.screen.right-30, y=play.screen.top-30, size=70)

#подсказки
text = play.new_text(words='Tap w to shoot, A/D to move', x=0, y=play.screen.bottom+60, font_size=40)

sea = play.new_box(
        color='blue', width=play.screen.width, height=50, x=0, y=play.screen.bottom+20
    )


@play.repeat_forever
async def game():
    global win
    global lose
    global pause
    if not (win or lose or pause):
        enemy=play.new_circle(radius=15,x=randint(-350,350),y=250)
        enemys.append(enemy)
        #тут опиши процесс игры
        await play.timer(seconds=2)

@play.repeat_forever
async def create_shield():
    global win
    global lose
    global pause
    if not (win or lose or pause):
        await play.timer(10)
        shields.append(play.new_circle(radius=15,x=randint(-350,350),y=250, color="violet"))

@play.repeat_forever
async def collide_shield():
    global win
    global lose
    global pause
    if not (win or lose or pause):
        for s in shields:
            if s.y<-300:
                shields.remove(s)
                s.remove()
            if chudik.is_touching(s):
                global should_count_lose_count
                should_count_lose_count = False
                sea.color = "violet"
                await play.timer(3)
                sea.color = "blue"
                should_count_lose_count = True      
@play.repeat_forever
def padenie():
    global win
    global lose
    global pause
    if not (win or lose or pause):
        for i in enemys:
            i.y-=3
@play.repeat_forever
async def blablabLA():
    global win
    global lose
    global pause
    if not (win or lose or pause):
        if play.key_is_pressed("w"):
            bullet=play.new_circle(radius=10,x=chudik.x,y=chudik.y, color="orange")
            bullets.append(bullet)
        #тут опиши процесс игры
        await play.timer(seconds=0.2)
@play.repeat_forever
def podem():
    global win
    global lose
    global pause
    if not (win or lose or pause):
        for i in bullets: 
            i.y+=7
        for s in shields:
            s.y-=2
@play.repeat_forever
def stolknowenie():
    global win
    global lose
    global pause
    if not (win or lose or pause):
        for enemy in enemys:
            for bullet in bullets:
                if enemy.is_touching(bullet):
                    enemys.remove(enemy)
                    bullets.remove(bullet)
                    bullet.remove()
                    enemy.remove()
                    chudik.win_count += 1

@play.repeat_forever
async def check_lose():
    global win
    global lose
    global pause
    if not (win or lose or pause):
        for b in enemys:
            if b.is_touching(sea):
                enemys.remove(b)
                b.remove()
                if should_count_lose_count:
                    chudik.lose_count += 1
                    score.words = str(chudik.lose_count)

@play.repeat_forever
def dwiganie():
    global win
    global lose
    global pause
    if not (win or lose or pause):
        if play.key_is_pressed("a"):
            chudik.x-=6
        elif play.key_is_pressed("d"):
            chudik.x+=6

@play.repeat_forever
def check_state():
    global win
    global lose
    global pause
    if chudik.lose_count >= 3:
        text.words = "You lose"
        text.color = "red"
        lose = True
    elif chudik.win_count >= 20:
        text.words = "You win"
        text.color = "green"
        win = True
    if play.key_is_pressed("1"):
        if pause:
            text.words = ""
        else:
            text.words = "Pause"
            text.color = "grey"
        pause = not pause
    
play.start_program()