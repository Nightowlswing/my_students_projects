import play

DINO=play.new_image("googe_dino.png", size=15)
balka=play.new_box(x=0,y=-150,color="grey",width=800,height=10)
#cactus=play.new_image("cactus.png",size=20)
DINO.start_physics(bounciness=0)
balka.start_physics(can_move=False)
cactuses=[]
cactuses.append(play.new_image("cactus.png",y=-130,x=800,size=14))
run = True

@play.repeat_forever
def jump():
    if DINO.is_touching(balka)and play.key_is_pressed("up"):
        DINO.physics.y_speed=50

bad_score=play.new_text(x=320,y=250,color='red', words="0")

@play.repeat_forever
async def do1():
    global run 
    if run:
        bad_score.words=str(int(bad_score.words)+1)
        await play.timer(0.1)


t = play.new_text(words="")
t.color="red"



@play.repeat_forever   
def move():
    if run:
        for c in cactuses: 
            c.x-=4 
            if c.x<-450:
                cactuses.remove(c)
                cactuses.append(play.new_image("cactus.png",y=-130,x=800,size=14))


@play.repeat_forever
def move():
    global run
    for c in cactuses:
        if c.is_touching(DINO):
            run = False           
            t.words="you lost this game..."
            

play.start_program()