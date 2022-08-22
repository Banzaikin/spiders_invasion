import pygame
from pygame.sprite import Sprite

class Spider(Sprite):
	#Класс для управления пауками
	def __init__ (self, ai_game):
		#Инициализирует пауков и создаёт их начальную позицию
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		#Загружает изображение пауков и получает прямоугольник
		self.image = pygame.image.load('images/mite-alt.png')
		self.rect = self.image.get_rect()
		#Пауки появляются в влевом верхнем углу экрана.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

	