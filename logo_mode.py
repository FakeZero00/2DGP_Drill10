from pico2d import *
import game_framework
import title_mode as next_mode

image = None
logo_start_time = 0

def init():
    global image, logo_start_time
    image = load_image("tuk_credit.png")
    logo_start_time = get_time()

def update():
    global logo_start_time
    if get_time() - logo_start_time > 2:
        game_framework.change_mode(next_mode)

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def finish():
    global image
    del image

def handle_events():
    event_list = get_events() #버퍼에서 이벤트 모두 가져옴
    #하지만 아무것도 하지 않는다. 즉, 버퍼에 인터럽트가 쌓이지 않게 한다.

def pause(): pass
def resume(): pass