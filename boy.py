from pico2d import *
import random
import numbers


global mouseevent

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    image = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3

    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.dir = 1
        self.run_frames = 0
        self.state = self.RIGHT_RUN
        if Boy.image == None:
            Boy.image = load_image('animation_sheet.png')

    def update(self):


        if self.state == self.RIGHT_RUN:
            self.frame = (self.frame + 1) % 8
            self.x += (self.dir * 5)
        elif self.state == self.LEFT_RUN:

            self.x += (self.dir * 5)

            self.frame = (self.frame + 1) % 8


        if self.state == self.RIGHT_STAND:
            self.frame = (self.frame + 1) % 8
        elif self.state == self.LEFT_STAND:
            self.frame = (self.frame + 1) % 8



        if self.x > 800:
            self.dir = -1
            self.x  = 800
            self.state = self.LEFT_RUN
        elif self.x < 0:
            self.dir = 1
            self.x = 0
            self.state = self.RIGHT_RUN
        if self.run_frames > 99:
            if self.run_frames < 150:
                if self.state == self.RIGHT_RUN:
                    self.state = self.RIGHT_STAND
                if self.state == self.LEFT_RUN:
                    self.state == self.LEFT_STAND
            if self.run_frames == 150:
                self.run_frames = 0
        if self.run_frames == 0:
            if self.state == self.LEFT_STAND:
                self.state = self.LEFT_RUN
            if self.state == self.RIGHT_STAND:
                self.state = self.RIGHT_RUN


    def draw(self):

        self.run_frames = self.run_frames + 1
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)



open_canvas()
boy = Boy()
grass = Grass()

team = [Boy() for i in range (1000)]





def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                pass
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
                pass
            if(event.type) == (SDL_MOUSEMOTION):
                mouseevent = event.x





global running
running = True
while running:
    handle_events()


    clear_canvas()
    grass.draw()

    for boy in team:
        boy.draw()
        boy.update()
    update_canvas()

    delay(0.05)






