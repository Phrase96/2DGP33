from pico2d import *
import game_framework
import title_state
import score_state



def Enter(self):
    open_canvas()
    global x
    global time
    time = 0
    x = 0


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        if event.type == SDL_MOUSEBUTTONDOWN:
            game_framework.push_state(score_state)


def doGameOver(score):
    entyr = score_state.Entry(score, time.time())


x += 10;
