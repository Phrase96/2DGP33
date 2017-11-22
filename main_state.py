import game_framework
from pico2d import *
import title_state
import random


class BG:

    def __init__(self):
        self.image = load_image('fresh-grass-with-sky-background_1149-1042.jpg')
    def draw(self):
        self.image.draw(400,300,800,1000)

class Fallen:
    sound = None
    image = None
    ef = None
    ef2 = None
    ef3 = None
    def __init__(self):
        self.x, self.y = random.randint(0, 800), random.randint(500, 100000)
        if Fallen.image == None:
            self.image = load_image('image_obstacle.png')
        self.frame = 1
        self.frame2 = 1
        self.state = 1
        self.stack = 1
        self.stack2 = 1
        self.speed = 10
        self.frame3 = 1
        self.frame4 = 1
        self.death = 0
        self.stack3 = 0
        self.add = -20
        if Fallen.sound == None:
            Fallen.sound = load_music('gb.mp3')
            Fallen.sound.set_volume(32)
        if Fallen.ef == None:
            Fallen.ef = load_image('fallen_ef.png')
        if Fallen.ef2 == None:
            Fallen.ef2 = load_image('fallen_ef.png')
        if Fallen.ef3 == None:
            Fallen.ef3 = load_image('fallen_ef.png')
    def Sound(self):
        self.sound.play()

    def update(self):
        self.y = self.y - self.speed
        self.frame4 += 1
        self.add += 2
        if self.add == 20:
            self.add = -20
        if self.frame4 == 3:
            self.frame4 =0

    def ex(self):
        self.effect2 = load_image('ex2.png')

    def exdraw(self):
        if self.state == 0:
            self.stack += 1
            self.effect2.clip_draw(110 * self.frame + 20, 125 * self.frame2, 110, 125, self.x, self.y)
            if self.stack == 14:
                self.state = 1
                self.stack = 0
                self.stack2 = 0



    def colide(self):
        if abs(car.x - self.x) < 25:
            if abs(car.y - self.y) < 25:
                self.death = 1
                self.Sound()

        if self.death == 1:
            self.stack3 += 1
            if self.stack3 == 35:
                game_framework.quit()

        if abs(self.y) < 50:
            self.frame = 0
            self.frame2 = 0
            self.state = 0
            self.speed = 0



    def draw(self):
        if self.state == 1:
            self.image.draw(self.x,self.y)
            self.ef.draw(self.x + random.randint(-40, 40),self.y + random.randint(-20, 20) + self.add)
            self.ef2.draw(self.x + random.randint(-40, 40), self.y + random.randint(-20, 20) + self.add)
            self.ef3.draw(self.x + random.randint(-40, 40), self.y + random.randint(-20, 20) + self.add)
        if self.state == 0:
            self.y = 110
            self.stack = self.stack + 1
            self.stack2 = self.stack2 + 1
            if self.stack2 == 4:
                if self.frame == 5:
                    self.frame2 = (self.frame2 + 1) % 3 + 1
                self.frame = (self.frame + 1) % 5 + 1

                self.stack2 = 1
            self.effect2.clip_draw(110 * self.frame, 150 * self.frame2, 110, 150 , self.x, self.y)
        if self.stack == 56:
            self.stack = 0
            self.state = 1
            self.y = 1000
            self.speed = random.randint(2, 25)

def enter():
    global bg
    bg = BG()
    global effect
    effect = Effect()
    global stack
    global stack2
    stack2 = 0
    stack = 10
    global fallen
    global group_fallen
    global car
    car = Car()
    group_fallen  = [Fallen() for i in range(100)]
    global grass
    grass = Grass()
    for fallen in group_fallen:
        fallen.ex()


class Effect:

    def __init__(self):
        self.x, self.y = 0, 0
        self.image = load_image('frame.png')
        self.frame = 1
        self.frame2 = 1
        self.boost = 0

    def update(self):
        self.x = car.x
        self.y = car.y
        if self.frame == 4:
            self.frame2 = (self.frame2 + 1) % 3 + 1
        self.frame = (self.frame + 1) % 3 + 1

    def draw(self):
        if car.state == 0:
            self.image.clip_draw(64 * self.frame, 64 * self.frame2, 64, 64, self.x + 45, self.y)
        if car.state == 1:
            self.image.clip_draw(64*self.frame, 64*self.frame2, 64, 64, self.x - 35, self.y)


class Car:


    def __init__(self):
        self.x, self.y = (400, 70)
        self.image = load_image('car_sprite2.png')
        self.frame3 = 1
        self.frame2 = 1
        self.leftstate = 1
        self.speed = 5
        self.state = 1




    def update(self):
        if self.speed == 0:
            self.speed = 5
        if self.frame2 == 3:
            self.frame3 = (self.frame3 + 1) % 3 + 1
        self.frame2 = (self.frame2 + 1) % 4
        if self.leftstate == 2:



            if self.x < 0:
                self.speed = 0;
            self.x -= self.speed


        if self.leftstate == 0:

            if self.x > 800:
                self.speed = 0

            self.x += self.speed




    def draw(self):
        if self.state == 1:
            self.image = load_image('car_sprite2.png')
        if self.state == 0:
            self.image = load_image('car_sprite3.png')
        self.image.clip_draw(70*self.frame2,35*self.frame3, 70, 30, self.x, self.y)





class Grass:
    def __init__(self):
        self.x, self.y = (400, 30)
        self.image = load_image('grass.png')
        self.bgm = load_music('11.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def draw(self):
        self.image.draw(self.x, self.y)


def exit():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                car.leftstate = 2
                car.state = 0
            elif event.key == SDLK_RIGHT:
                car.leftstate = 0
                car.state = 1
            if event.key == SDLK_SPACE:
                car.speed = 10
                effect.boost = 1
        if event.type == SDL_KEYUP:
            if event.key == SDLK_SPACE:
                car.speed = 5
                effect.boost = 0
            if event.key == SDLK_LEFT:
                car.leftstate = 1
            if event.key == SDLK_RIGHT:
                car.leftstate = 1


def update():
    for fallen in group_fallen:
        fallen.colide()
        fallen.update()
    fallen.update()
    car.update()
    effect.update()
    delay(0.01)

def draw():
    clear_canvas()
    bg.draw()
    if effect.boost == 1:
        effect.draw()
    car.draw()
    grass.draw()

    for fallen in group_fallen:
        fallen.draw()
    update_canvas()