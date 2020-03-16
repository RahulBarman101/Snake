import pygame
import random

body = []
pygame.init()
pygame.display.set_caption('Snake Game!!!')

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)

win_height = 600
win_width = 800

win = pygame.display.set_mode((win_width,win_height))
game_over = False

x1 = win_width//2
y1 = win_height//2
x1_change = 0
y1_change = 0

score_font = pygame.font.SysFont("comicsansms", 35)

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

foodx = (random.choice([i for i in range(win_width-snake_block)])//snake_block)*snake_block
foody = (random.choice([i for i in range(win_height-snake_block)])//snake_block)*snake_block

snake_list = []
Length_of_snake = 1

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x1_change = -snake_block
				y1_change = 0

			elif event.key == pygame.K_RIGHT:
				x1_change = snake_block
				y1_change = 0

			elif event.key == pygame.K_UP:
				x1_change = 0
				y1_change = -snake_block

			elif event.key == pygame.K_DOWN:
				x1_change = 0
				y1_change = snake_block

	x1 += x1_change
	y1 += y1_change
	
	win.fill(black)
	pygame.draw.rect(win,blue,[foodx,foody,snake_block,snake_block])
	snake_head = []
	snake_head.append(x1)
	snake_head.append(y1)
	snake_list.append(snake_head)

	if len(snake_list) > Length_of_snake:
		del snake_list[0]

	if snake_head in snake_list[:-1]:
		pygame.quit()

	for i in snake_list:
		pygame.draw.rect(win,red,[i[0],i[1],snake_block,snake_block])

	value = score_font.render(f"Score: {Length_of_snake-1}",True,white)
	win.blit(value,[0,0])

	pygame.display.update()

	if x1 == 0 or x1 == win_width-snake_block:
		while True:
			win.fill(blue)
			val = score_font.render(f'You Lost!!!\n\nScore: {Length_of_snake-1}',True,white)
			win.blit(val,[win_width/6,win_height/6])
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						pygame.quit() 

	if y1 == 0 or y1 == win_height-snake_block:
		while True:
			win.fill(blue)
			val = score_font.render(f'You Lost!!!\n\nScore: {Length_of_snake-1}',True,white)
			win.blit(val,[win_width/6,win_height/6])
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						pygame.quit()

	if x1 == foodx and y1 == foody:
		foodx = (random.choice([i for i in range(snake_block*2,win_width-snake_block)])//snake_block)*snake_block
		foody = (random.choice([i for i in range(snake_block*2,win_height-snake_block)])//snake_block)*snake_block
		print('yumm!!!')
		Length_of_snake += 1

	clock.tick(snake_speed)