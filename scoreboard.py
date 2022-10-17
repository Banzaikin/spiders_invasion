import pygame.font
from pygame.sprite import Group
from pygame.sprite import Sprite
from ship import Ship

class Scoreboard(Sprite):
	#Класс для вывода игровой информации
	def __init__(self, ai_game):
			#Иициализирует атрибуты подстчета очков
		super().__init__()
		self.ai_game = ai_game
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = ai_game.settings
		self.stats = ai_game.stats

		#Настройки шрифта для вывода счёта
		self.text_color = (0, 0, 255)
		self.font = pygame.font.SysFont(None, 48)
		#Подготовка исходного изображения
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()

	def prep_score(self):
		#Преобразует текующий счёт в графичесоке изображение
		rounded_score = round(self.stats.score, -1)
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True, self.text_color, 
											self.settings.rgb_color)
		#Вывод счёта в правом верхнем углу экрана
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def prep_high_score(self):
		#Преобразует рекордный счет в графическое изображение
		high_score = round(self.stats.high_score, -1)
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True,
								self.text_color, self.settings.rgb_color)
		#Рекорд выравнивается по центру верхней стороны
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top

	def check_high_score(self):
		#Проверяет больше ли счёт рекорда
		if self.stats.score > self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.prep_high_score()

	def prep_level(self):
		#Преобразует уровень в графическое изображение
		level_str = str(self.stats.level)
		self.level_image = self.font.render(level_str, True,
							self.text_color, self.settings.rgb_color)
		#Уровень выводится под текущим счётом
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10

	def prep_ships(self):
		#Сообщает кол-во оставшихся кораблей
		ships_str = str(self.stats.ships)
		self.ships_image = self.font.render(ships_str, True,
							self.text_color, self.settings.rgb_color)
		#Уровень выводится под текущим счётом
		self.ships_rect = self.ships_image.get_rect()
		self.ships_rect.left = self.screen_rect.left + 10
		self.ships_rect.top = self.ships_rect.top + 20

	def show_score(self):
		#Выводит счёт, уровень, жизни и рекорд на экран
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.screen.blit(self.ships_image, self.ships_rect)