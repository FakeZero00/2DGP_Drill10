from pico2d import *
import game_framework
import play_mode
from pannel import Pannel
import game_world

def init():
    global pannel

    pannel = Pannel()
    game_world.add_object(pannel, 2)

def update():
    game_world.update() #플레이 모드 유지

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def finish():
    global pannel
    game_world.remove_object(pannel)
    del pannel

def handle_events():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_0:
                play_mode.boy.item = None
            elif event.key == SDLK_1:
                play_mode.boy.item = 'Ball'
            elif event.key == SDLK_2:
                play_mode.boy.item = 'BigBall'
            elif event.key == SDLK_i:
                game_framework.pop_mode()

def pause(): pass
def resume(): pass