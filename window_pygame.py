import sys
import pygame
from settings import Settings
from ship import Ship

class WindowPygame:
	#Класс для управлением ресурсами и поведением игры

	def __init__(self):
		#Функция прорисовки экрана
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(screen)
		#При каждом проходе цикла перерисовывается экран
		self.screen.fill(self.settings.rgb_color)
		self.ship.blitme()
		#Отображение последнего прорисованного экрана
		pygame.display.flip()

	def run_game(self):
		#Функция для запуска основного цикла игры
		while True:
			#Отслеживание движений мыши и клавиатуры
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()


if __name__ == '__main__':
	#Создание экземпляра и запуск игры
	ai = WindowPygame()
	ai.run_game()
