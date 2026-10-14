from pico2d import *
import random


# Game object class here

class Ball_2():
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('ball21x21.png')
    def update(self):
        self.frame = (self.frame + 1) % 1
        self.y += 8

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Ball_1():
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('ball41x41.png')
    def update(self):
        self.frame = (self.frame + 1) % 1
        self.y += 3

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)
    def update(self):
        pass    

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

def reset_world():
    global running
    global world
    global ball_1
    global ball_2

    running = True
    world = []
    global grass
    grass = Grass()
    world.append(grass)
    global team
    global team2
    global team3
    
    team = [Boy() for i in range(10)]
    team2 = [Ball_1() for i in range(10)]
    team3 = [Ball_2() for i in range(10)]

    world += team
    world += team2
    world += team3

    ball_1 = Ball_1()
    ball_2 = Ball_2()

    world.append(ball_1)
    world.append(ball_2)


def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False




open_canvas()

reset_world()
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)


close_canvas()
