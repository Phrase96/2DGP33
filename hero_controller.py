def update(self):
    self.frame = (self.frame + 1) % 8
    if self.state == self.RIGHT_RUN:
        self.x = min(800, self.x + 5)
    elif self.state == self.LEFT_RUN:
        self.x = max(0, self.x - 5)

def handle_events():
    global running
    global hero
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            runngin = False
        elif (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            running = False
        else:
            hero.handle_event(event)