class Settings():
	#Класс для хранения всех настроек игры

	def __init__(self):
		#Параметры экрана
		self.screen_width = 1200
		self.screen_height = 800
		self.rgb_color = ( 0, 0, 0 )
		#Настройки корабля
		self.ship_speed = 3
		self.ships_limit = 3
		#Параметры выстрелов
		self.bullet_speed = 5
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (255, 0, 0)
		self.bullet_allowed = 5
		#Параметры пауков
		self.spider_speed = 1
		self.fleet_drop_speed = 10
		self.fleet_direction = 1
		#Темп ускорения игры
		self.speedup_scale = 10
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		#Инициализирует настройки, изменяющиеся в ходе игры
		self.ship_speed_factor = 10
		self.bullet_speed_factor = 10
		self.spider_speed_factor = 10
		self.fleet_direction = 1

	def increase_speed(self):
		#Увеличивает настройки скорости
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.spider_speed_factor *= self.speedup_scale