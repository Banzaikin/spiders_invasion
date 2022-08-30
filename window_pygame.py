import sys
from time import sleep
import pygame

from settings import Settings
from game_status import GameStats
from button import Button
from ship import Ship
from stars import Star
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
		pygame.display.set_caption("Планета пауков")
		#Создание экземпляра для хранения игровой статистики
		self.stats = GameStats(self)
		self.ship = Ship(self)
		self.stars = pygame.sprite.Group()
		self.bullets = pygame.sprite.Group()
		self.spiders = pygame.sprite.Group()

		#Игра запускается в активном состоянии
		self.stats.game_active = False

		self._create_star()
		self._create_fleet()

		#Создание кнопки Play
		self.play_button = Button(self, "Play")
		
	def run_game(self):
		#Функция для запуска основного цикла игры
		while True:
			self._check_events()
			
			if self.stats.game_active:
				self.ship.update()
				self._update_bullets()
				self._update_spiders()

			self._update_screen()

	def _create_star(self):
		#Создание звезд
		for star_number in range(0,100):
			if 1 == 1:
				star = Star(self)
				self.stars.add(star)
		
		
	def _check_events(self):
		#Отслеживание движений мыши и клавиатуры
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)

	def _check_play_button(self, mouse_pos):
		#Запускает игру при нажатии на кнопку Play
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.stats.game_active:
			#Сброс игровых настроек
			self.settings.initialize_dynamic_settings()
			#Сброс игровой статистики в данном раунде
			self.stats.reset_stats()
			self.stats.game_active = True
			#Очистка спсиков пауков и снарядов
			self.spiders.empty()
			self.bullets.empty()
			#Создание нового корабля и противников
			self._create_fleet()
			self.ship.center_ship()
			#Указатель мыши скрывается
			pygame.mouse.set_visible(False)
					
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

		self._check_bullet_spider_collisions()

	def _check_bullet_spider_collisions(self):
		#При обнаружении попадания в пришельца удаляет снаряд и пришельца
		collisions = pygame.sprite.groupcollide(
				self.bullets, self.spiders, True, True)
		if not self.spiders:
			#Уничтожение существующих снарядов и создание нового отряда пауков
			self.bullets.empty()
			self._create_fleet()
			self.settings.increase_speed()

	def _update_spiders(self):
		#Обновляет позиции пауков
		self._check_fleet_edges()
		self.spiders.update()

		#Проверка коллизий пауков с кораблем
		if pygame.sprite.spritecollideany(self.ship, self.spiders):
			self._ship_hit()

		#Проверяет добрались ли пауки до нижнего края экрана
		self._check_spiders_bottom()

	def _create_fleet(self):
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

	def _check_fleet_edges(self):
		#Реагирует на достижение пауком экрана
		for spider in self.spiders.sprites():
			if spider.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		#Опускает весь флот и изменяет направление движения
		for spider in self.spiders.sprites():
			spider.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1

	def _ship_hit(self):
		#Обрабатывает столкновения корабля с пауками
		if self.stats.ships_left > 0:
			self.stats.ships_left -= 1
			#Очистка списков пауков и снарядов
			self.spiders.empty()
			self.bullets.empty()
			#Создание новой группы пауков и размещение корабля в центре
			self._create_fleet()
			self.ship.center_ship()
			#Пауза
			sleep(0.5)
		else:
			self.stats.game_active = False
			pygame.mouse.set_visible(True)

	def _check_spiders_bottom(self):
		#Проверяет добрались ли пауки до нижнего края экрана
		screen_rect = self.screen.get_rect()
		for spider in self.spiders.sprites():
			if spider.rect.bottom >= screen_rect.bottom:
				#Теряется жизнь
				self._ship_hit()
				break

	def _update_screen(self):
		#При каждом проходе цикла перерисовывается экран
			self.screen.fill(self.settings.rgb_color)
			self.ship.blitme()
			self.stars.draw(self.screen)
			for bullet in self.bullets.sprites():
				bullet.draw_bullet()
			self.spiders.draw(self.screen)
			#Кнопка Play отображается только в том случае, если игра неактивна
			if not self.stats.game_active:
				self.play_button.draw_button()
			#Отображение последнего прорисованного экрана
			pygame.display.flip()

if __name__ == '__main__':
	#Создание экземпляра и запуск игры
	ai = WindowPygame()
	ai.run_game()
