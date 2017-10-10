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
    stack = 10
    global fallen
    global group_fallen
    group_fallen  = [Fallen() for i in range(100)]




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
    delay(0.01)

def draw():
    clear_canvas()
    for fallen in group_fallen:
        fallen.draw()
    update_canvas()