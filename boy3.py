import random
from pico2d import *



class Background:
    def __init__(self):
        self.image = load_image('background.png')
        self.left = 1
        self.screen_width = 800
        self.screen_height = 600
        self.speed = 10
        self.SCROLL_SPEED_PPS = 10
        self.frame_speed = 0



    def draw(self):
        x = int(self.left)
        w = min(self.image.w - x, self.screen_width)
        self.image.clip_draw_to_origin(x, 0, w, self.screen_height, 0 , 0)
        self.image.clip_draw_to_origin(0,0, self.screen_width - w, self.screen_height, w, 0)


    def update(self):
        self.left = (self.left + self.frame_speed * self.speed) % self.image.w

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

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
    global grass, running, boy, bg
    boy = Boy()
    grass = Grass()
    running = True
    bg = Background()








def handle_events(self):
    global running

    events = get_events()

    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                self.frame_speed = -1
            elif event.key == SDLK_RIGHT:
                self.frame_speed = 1
        if event.type == SDL_KEYUP:
            self.frame_speed = 0






def update():
    bg.update()
    boy.update()

    delay(0.01)


def draw():
    clear_canvas()
    bg.draw()
    boy.draw()
    grass.draw()
    update_canvas()



def main():

    open_canvas()
    enter()

    while running:
        handle_events(bg)
        draw()
        update()

    close_canvas()


if __name__ == '__main__':
    main()