nmae = 'titlestate'
image = None
import game_framework
import main_state
from pico2d import *

def enter():
    global image
    image = load_image('title.png')

def exit():
    global image
    del(image)

def update():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_f):
                game_framework.change_state(main_state)

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()