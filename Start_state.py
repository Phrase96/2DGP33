
name = "start_state"
image = None
logo_time = 0.0
def enter():
	global image
	open_canvas()
	Image = load_image('kpu_credit.png')

	
def exit():
	global image
	del(image)
	close_canvas()

	
def update():
	global logo_time

	
def update():
	global logo_time
	if (logo_time > 1.0):
		logo_time = 0
		game_framework.quit()
	delay(0.01)
	logo_time += 0.01

	
def draw():
	global image
	clear_canvas()
	image.draw(400, 300)
	update_canvas()

	

