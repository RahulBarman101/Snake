import pygame
import random

class snake:
	def __init__(self):
		pygame.init()
		self.black = (0,0,0)
		self.red = (255,0,0)
		self.white = (255,255,255)
		self.blue = (0,0,255)
		self.height = 500
		self.width = 800
		self.x1 = self.width//2
		self.y1 = self.height//2
		self.changex = 0
		self.changey = 0
		self.snake_block = 10
		self.snake_speed = 15
		self.foodx = (random.choice([i for i in range(self.snake_block,500-self.snake_block)])//self.snake_block)*self.snake_block
		self.foody = (random.choice([i for i in range(self.snake_block,500-self.snake_block)])//self.snake_block)*self.snake_block
		self.body = []
		self.length_of_snake = 1
		self.score = 0

		self.clock = pygame.time.Clock()
		
		# self.play(win)

	def play(self):

		surface = pygame.display.set_mode((self.width,self.height))
		pygame.display.set_caption('Snake Game!!!')
		self.redrawWin(surface)
		game_over = False

		while not game_over:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						self.changex = -self.snake_block
						self.changey = 0
					elif event.key == pygame.K_RIGHT:
						self.changex = self.snake_block
						self.changey = 0
					elif event.key == pygame.K_UP:
						self.changex = 0
						self.changey = -self.snake_block
					elif event.key == pygame.K_DOWN:
						self.changex = 0
						self.changey = self.snake_block

			head = []
			self.x1 += self.changex
			self.y1 += self.changey
			surface.fill(self.black)
			head.append(self.x1)
			head.append(self.y1)
			self.body.append(head)

			if len(self.body) > self.length_of_snake:
				del self.body[0]

			self.draw(self.foodx,self.foody,surface,self.blue)

			if head in self.body[:-1]:
				pygame.quit()

			for i in self.body:
				self.draw(i[0],i[1],surface,self.red)

			if self.x1 == self.foodx and self.y1 == self.foody:
				self.foodx = (random.choice([i for i in range(self.snake_block,500-self.snake_block)])//self.snake_block)*self.snake_block
				self.foody = (random.choice([i for i in range(self.snake_block,500-self.snake_block)])//self.snake_block)*self.snake_block
				print('yumm!!!')
				self.length_of_snake += 1
				self.score += 1
				
			if self.x1 == 0 or self.y1 == 0:
				pygame.quit()
			elif self.x1 == self.width-self.snake_block or self.y1 == self.height-self.snake_block:
				pygame.quit()

			self.clock.tick(self.snake_speed)


	def redrawWin(self,surface):
		surface.fill(self.black)
		pygame.display.update()

	def draw(self,x,y,surface,color):
		pygame.draw.rect(surface,color,(x,y,self.snake_block,self.snake_block))
		pygame.display.update()

s = snake()
s.play()
	