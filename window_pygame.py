import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from spider import Spider

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
		self.spiders = pygame.sprite.Group()

		self._create_fleat()
		pygame.display.set_caption("Планета пауков")

	def run_game(self):
		#Функция для запуска основного цикла игры
		while True:
			self._check_events()
			self.ship.update()
			self._update_bullets()
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
		if len(self.bullets) < self.settings.bullet_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		#Обновляет позиции снарядов и уничтожает старые снаряды
		self.bullets.update()

		for bullet in self.bullets.copy():
				if bullet.rect.bottom <= 0:
					self.bullets.remove(bullet)

	def _create_fleat(self):
		#Создание группы пауков
		#Определение ряда для размещения пауков
		spider = Spider(self)
		spider_width, spider_height = spider.rect.size
		available_space_x = self.settings.screen_width - (2 * spider_width)
		number_spiders_x = available_space_x // (2 * spider_width)

		#Определение колличества рядов, помещающихся на экране
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height -
								(3 * spider_height)) - ship_height
		number_rows = available_space_y // (2 * spider_height)

		#Создание пауков
		for row_number in range(number_rows):
			for spider_number in range(number_spiders_x):
				self._create_spider(spider_number, row_number)

	def _create_spider(self, spider_number, row_number):
		#Создание пауков и размещение их в ряду
		spider = Spider(self)
		spider_width, spider_height = spider.rect.size
		spider_width = spider.rect.width
		spider.x = spider_width + 2 * spider_width * spider_number
		spider.rect.x = spider.x
		spider.rect.y = spider.rect.height + 2 * spider.rect.height * row_number
		self.spiders.add(spider)

	def _update_screen(self):
		#При каждом проходе цикла перерисовывается экран
			self.screen.fill(self.settings.rgb_color)
			self.ship.blitme()
			for bullet in self.bullets.sprites():
				bullet.draw_bullet()
			self.spiders.draw(self.screen)
			#Отображение последнего прорисованного экрана
			pygame.display.flip()

if __name__ == '__main__':
	#Создание экземпляра и запуск игры
	ai = WindowPygame()
	ai.run_game()
