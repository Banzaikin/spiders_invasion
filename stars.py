import pygame
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):
	#Создает звезды на фоне
	
	def __init__(self, ai_game):
		#Инициализирует звёзды и создаёт их начальную позицию
		super().__init__()
		self.screen = ai_game.screen
		
		#Загружает звезды на фоне
		self.image = pygame.image.load('images/polar-star.png')
		self.rect = self.image.get_rect()
		
		#Каждая звезда появляется в левом верхнем углу
		self.rect.x = randint(0,1200)
		self.rect.y = randint(0,800)