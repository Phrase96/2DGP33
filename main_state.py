import game_framework
from pico2d import *
import title_state
import random



class Fallen:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), random.randint(500, 100000)
        self.image = load_image('falling_object_120623_172119.png')

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
        self.image = load_image('car_sprite.png')
        self.frmae3 = 0
        self.frame2 = 1

    def update(self):
        self.x += 2


    def draw(self):
        self.image.clip_draw(72,60, 70, 35, self.x, self.y)



class Grass:
    def __init__(self):
        self.x, self.y = (400, 30)
        self.image = load_image('grass.png')

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