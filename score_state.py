from pico2d import *
import json
import game_framework
import pickle
import my_game2

class Entry:
    def __init__(self, score, time):
        self.score = score
        self.time = time


name = "ScoreState"

usesPickle = True
if(usesPickle):
    fileName = 'score.pickle'
else:
    fileName = "score.json"



def LoadScores():
    global scores
    scores = []
    if (usesPickle):
        f = open("scores.txt", 'rb')
        scores = pickle.load(f)
        f.close()
        print("Scores:", scores)

def SaveScroes():
    global scores
    if (usesPickle):
        f = open("score.txt", 'wb')
        pickle.dump(scores, f)
        f.close()



scores = []
LoadScores()






def add(score):
    global scores
    print("Now scores had" + str(len(scores)) + "entries")
    scores.append(score)
    print("Now scores has" + str(len(scores)) + "entries")
    SaveScroes()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        if event.type == SDL_MOUSEBUTTONDOWN:
            game_framework.pop_state(my_game2)

font = None
def enter():
    print("NOw ScoreState")
    pass

def exit():
    print("Leaves ScoreSTate")
    pass

def draw():
    clear_canvas()

def update():
    pass



