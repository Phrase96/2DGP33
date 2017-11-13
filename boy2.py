from pico2d import *
import game_framework
import random
import numbers
import json_player


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Background:
    def __init__(self):
        self.image = load_image('background.png')
        self.left = 0
        self.screen_width = 800
        self.screen_height = 600
        self.speed = 10
        self.SCROLL_SPEED_PPS = 10



    def draw(self):
        x = int(self.left)
        w = min(self.image.w - x, self.screen_width)
        self.image.clip_draw_to_origin(x, 0, w, self.screen_height, 0 , 0)
        self.image.clip_draw_to_origin(0,0, self.screen_width - w, self.screen_height, w, 0)


    def update(self):
        self.left = (self.left * self.speed) % self.image.w

class Ball:
    image = None;

    def __init__(self):
        self.x, self.y = random.randint(200, 790), 60
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x -10, self.y - 10, self.x + 10, self.y + 10


def create_world():
    global boy, grass, balls, bg
    boy = Boy()
    balls = [Ball() for i in range (10)]
    grass = Grass()
    bg = Background()


def handle_events(self):
     global running
     global chr_st
     global team
     event = get_events()
     if event.type == SDL_KEYDOWN:
         if event.key == SDLK_LEFT:
             self.speed -= 10
         elif event.key == SDLK_RIGHT:
             self.speed += 10
     if event.type == SDL_KEYUP:
         if event.key == SDLK_LEFT:
             self.speed += 10
         elif event.key == SDLK_RIGHT:
             self.speed -= 10





class Boy:
    image = None

    def get_bb(self):
        return self.x - 20, self.y - 40, self.x + 20, self.y + 40

    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)




        if Boy.image == None:
            Boy.image = load_image('animation_sheet.png')




    def update(self):
        self.frame = (self.frame + 1) % 8


    def draw(self):
        self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)


def enter():
    global team, grass, chr_st, running, balls, boy, bg
    i = 0
    boy = Boy()
    grass = Grass()
    balls = [Ball() for i in range(10)]
    chr_st = -1
    running = True
    bg = Background()

def exit():
    global team, grass, chr_st, running
    del (team)
    del (grass)
    del (chr_st)
    del (running)





def update():
    global team


    bg.update()
    boy.update()



    delay(0.01)


def draw():
    global chr_st
    clear_canvas()
    bg.draw()

    boy.draw()

    grass.draw()

    numbers.draw(0, 740, 540,1)
    update_canvas()





def main():

    open_canvas()
    enter()


    global running

    while running:

        handle_events(bg)
        draw()
        update()

    close_canvas()


if __name__ == '__main__':
    main()