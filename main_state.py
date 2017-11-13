import game_framework
from pico2d import *
import title_state
import random



class Fallen:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), random.randint(500, 100000)
        self.image = load_image('image_obstacle.png')

    def update(self):
        self.y = self.y - 10;

    def draw(self):
        self.image.draw(self.x,self.y)

def enter():
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


class Car:


    def __init__(self):
        self.x, self.y = (400, 70)
        self.image = load_image('car_sprite2.png')
        self.frame3 = 1
        self.frame2 = 1
        self.leftstate = 1
        self.speed = 5

    def update(self):
        if self.frame2 == 3:
            self.frame3 = (self.frame3 + 1) % 3 + 1
        self.frame2 = (self.frame2 + 1) % 4
        if self.leftstate == 2:
            self.x -= self.speed
        if self.leftstate == 0:
            self.x += self.speed




    def draw(self):
        self.image.clip_draw(70*self.frame2,35*self.frame3, 70, 30, self.x, self.y)






class Grass:
    def __init__(self):
        self.x, self.y = (400, 30)
        self.image = load_image('grass.png')
        self.bgm = load_music('football.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def draw(self):
        self.image.draw(self.x, self.y)


def exit():
    global fallen
    del(fallen)

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
            elif event.key == SDLK_RIGHT:
                car.leftstate = 0
            if event.key == SDLK_SPACE:
                car.speed = 10
        if event.type == SDL_KEYUP:
            if event.key == SDLK_SPACE:
                car.speed = 5
            if event.key == SDLK_LEFT:
                car.leftstate = 1
            if event.key == SDLK_RIGHT:
                car.leftstate = 1


def update():
    for fallen in group_fallen:
        fallen.update()
    fallen.update()
    car.update()
    delay(0.01)

def draw():
    clear_canvas()
    car.draw()
    grass.draw()
    for fallen in group_fallen:
        fallen.draw()
    update_canvas()