import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self, ai_game):
		#Создает объект снарядов в текущей позиции корабля
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color
		#Создание снаряда в нулевой позиции и назначении его в правильной позиции
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
			self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop
		#Перевод позиции снаряда из целочисленного в вещественный формат
		self.y = float(self.rect.y)

	def update(self):
		#Отвечает за перемещение снаряда
		self.y -= self.settings.bullet_speed
		self.rect.y = self.y 

	def draw_bullet(self):
		#Вывод снарядов на экран
		pygame.draw.rect(self.screen, self.color, self.rect)