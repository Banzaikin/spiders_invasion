import sys
import os
import pygame
from pygame.sprite import Sprite
from random import randint

def resource_path(relative_path):
	#Функция загрузки файлов в файл .exe
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Star(Sprite):
	#Создает звезды на фоне
	
	def __init__(self, ai_game):
		#Инициализирует звёзды и создаёт их начальную позицию
		super().__init__()
		self.screen = ai_game.screen
		
		#Загружает звезды на фоне
		self.image = pygame.image.load(resource_path('images/polar-star.png'))
		self.rect = self.image.get_rect()
		
		#Каждая звезда появляется в левом верхнем углу
		self.rect.x = randint(0,1200)
		self.rect.y = randint(0,800)