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

class Ball:
    image = None;

    def __init__(self):
        self.x, self.y = random.radint(200, 790), 60
        if Ball.image == None:
            Ball.image = load_image('')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x -10, self.y - 10, self.x + 10, self.y + 10


def create_world():
    global boy, grass, balls
    boy = Boy()
    balls = [Ball() for i in range (10)]
    grass = Grass()

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False
    return True






class Boy:
    image = None

    COUNT_NUM = 1

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3

    PIXEL_PER_METER = (10.0/0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 /60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM/ 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def get_bb(self):
        return self.x - 20, self.y - 40, self.x + 20, self.y + 40

    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.state = self.RIGHT_RUN
        self.run_frames, self.stand_frames = 0, 0
        self.num = Boy.COUNT_NUM
        Boy.COUNT_NUM += 1

        if Boy.image == None:
            Boy.image = load_image('animation_sheet.png')

    def handle_left_run(self):
        self.x -= 5
        self.run_frames += 1

        if self.x < 0:
            self.state = self.RIGHT_RUN
            self.x = 0
            self.frame = 0
        if self.run_frames == 100:
            self.state = self.LEFT_STAND
            self.stand_frames = 0
            self.frame = 0

    def handle_left_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 50:
            self.state = self.LEFT_RUN
            self.run_frames = 0
            self.frame = 0

    def handle_right_run(self):
        self.x += 5
        self.run_frames += 1
        if self.x > 800:
            self.state = self.LEFT_RUN
            self.x = 800
            self.frame = 0
        if self.run_frames == 100:
            self.state = self.RIGHT_STAND
            self.stand_frames = 0
            self.frame = 0

    def handle_right_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 50:
            self.state = self.RIGHT_RUN
            self.run_frames = 0
            self.frame = 0

    handle_state = {LEFT_RUN: handle_left_run, RIGHT_RUN: handle_right_run, LEFT_STAND: handle_left_stand,
                    RIGHT_STAND: handle_right_stand}

    def update(self):
        self.frame = (self.frame + 1) % 8
        if self.state == self.RIGHT_RUN:
            self.x = min(800, self.x + 5)
        elif self.state == self.LEFT_RUN:
            self.x = max(0, self.x - 5)
        self.handle_state[self.state](self)

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)

        numbers.draw(self.num, self.x + 50, self.y, 0.3)


def enter():
    global team, grass, chr_st, running, balls
    i = 0
    team = [Boy() for i in range(1000)]
    grass = Grass()
    balls = [Ball() for i in range(10)]
    chr_st = -1
    running = True


def exit():
    global team, grass, chr_st, running
    del (team)
    del (grass)
    del (chr_st)
    del (running)


def handle_events(self):
    global running
    global chr_st
    global team
    events = get_events()





    for event in events:
        global keystate
        keystate = 0
        if team[chr_st].state == team[chr_st].RIGHT_RUN:
            team[chr_st].state = team[chr_st].RIGHT_STAND
        if team[chr_st].state == team[chr_st].LEFT_RUN:
            team[chr_st].state = team[chr_st].LEFT_STAND

        if event.type == SDL_QUIT:
            running = False
            game_framework.quit()

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
                game_framework.pop_state()

            elif event.key == SDLK_UP:
                chr_st += 1
                if chr_st > 999:
                    chr_st = 0

            elif event.key == SDLK_DOWN:
                chr_st -= 1
                if chr_st < 0:
                    chr_st = 999

            if event.key == SDLK_RIGHT:
                if event.type == SDL_KEYDOWN:
                    team[chr_st].state = team[chr_st].RIGHT_RUN
                else:
                    team[chr_st].state = team[chr_st].RIGHT_STAND

            if event.key == SDLK_LEFT:
                if event.type == SDL_KEYDOWN:
                    team[chr_st].state = team[chr_st].LEFT_RUN
                else:
                    team[chr_st].state = team[chr_st].LEFT_STAND











        elif event.type == SDL_MOUSEMOTION and chr_st >= 0:
            team[chr_st].x = event.x
            team[chr_st].y = 600 - event.y




def update():
    global team

    for boy in team:
        boy.update()

    for ball in balls:
        ball.update()

    for ball in balls:
        if collide(boy, ball):
            print("cllision")

    delay(0.01)


def draw():
    global chr_st
    clear_canvas()

    for boy in team:
        boy.draw()

    grass.draw()

    numbers.draw(0, 740, 540,1)
    update_canvas()


def main():

    open_canvas()
    enter()

    global running

    while running:
        handle_events(team[chr_st])
        draw()
        update()

    close_canvas()


if __name__ == '__main__':
    main()
