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
		#Перевод координаты паука из целочисленого в вещественное
		self.rect.x = float(self.rect.x)
		self. rect.y = float(self.rect.y)
	
	def check_edges(self):
		#Возвращает True, если паук находится у края экрана
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True

	def update(self):
		#Перемещает пауков вправо и влево
		self.x += (self.settings.spider_speed * self.settings.fleet_direction)
		self.rect.x = self.x

