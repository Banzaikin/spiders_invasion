import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class WindowPygame:
	#Класс для управлением ресурсами и поведением игры

	def __init__(self):
		#Функция прорисовки экрана
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		pygame.display.set_caption("Космическое вторжение")

	def run_game(self):
		#Функция для запуска основного цикла игры
		while True:
			self._check_events()
			self.ship.update()
			self.bullets.update

			#Удаление снарядов, вышедших за верхний край экрана
			for bullet in self.bullets.copy():
				if bullet.rect.bottom <= 0:
					self.bullets.remove(bullet)
					
			self._update_screen()
			
	def _check_events(self):
		#Отслеживание движений мыши и клавиатуры
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
					
	def _check_keydown_events(self, event):
		#Реагирует на нажатие клавиш
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		#Закрытие игры с помощью кнопки Esc
		elif event.key == pygame.K_ESCAPE:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		#Реагирует на отпусание клавиш
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False
		elif event.key == pygame.K_UP:
			self.ship.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False

	def _fire_bullet(self):
		#Создание нового снаряда и включение его в группу bullets
		new_bullet = Bullet(self)
		self.bullets.add(new_bullet)

	def _update_screen(self):
		#При каждом проходе цикла перерисовывается экран
			self.screen.fill(self.settings.rgb_color)
			self.ship.blitme()
			for bullet in self.bullets.sprites():
				bullet.draw_bullet()
			#Отображение последнего прорисованного экрана
			pygame.display.flip()

if __name__ == '__main__':
	#Создание экземпляра и запуск игры
	ai = WindowPygame()
	ai.run_game()
