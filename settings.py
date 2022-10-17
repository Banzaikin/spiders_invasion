class Settings():
	#Класс для хранения всех настроек игры

	def __init__(self):
		#Параметры экрана
		self.screen_width = 1200
		self.screen_height = 800
		self.rgb_color = ( 0, 0, 0 )
		#Настройки корабля
		self.ships_limit = 3
		#Параметры выстрелов
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (255, 0, 0)
		self.bullet_allowed = 5
		#Параметры пауков
		self.fleet_drop_speed = 10
		#Темп ускорения игры
		self.speedup_scale = 1.1
		self.initialize_dynamic_settings()
		#Темп роста стоимости пауков
		self.score_scale = 1.5

	def initialize_dynamic_settings(self):
		#Инициализирует настройки, изменяющиеся в ходе игры
		self.ship_speed_factor = 2
		self.bullet_speed_factor = 3
		self.spider_speed_factor = 1
		self.fleet_direction = 1
		self.spider_points = 10

	def increase_speed(self):
		#Увеличивает настройки скорости и стоимости пауков
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.spider_speed_factor *= self.speedup_scale
		self.spider_points = int(self.spider_points * self.score_scale)