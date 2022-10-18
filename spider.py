import sys
import os
import pygame
from pygame.sprite import Sprite

def resource_path(relative_path):
	#Функция загрузки файлов в файл .exe
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Spider(Sprite):
	#Класс для управления пауками
	def __init__ (self, ai_game):
		#Инициализирует пауков и создаёт их начальную позицию
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		#Загружает изображение пауков и получает прямоугольник
		self.image = pygame.image.load(resource_path('images/mite-alt.png'))
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
		self.x += (self.settings.spider_speed_factor * 
												self.settings.fleet_direction)
		self.rect.x = self.x

