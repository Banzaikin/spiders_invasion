class Settings():
	#Класс для хранения всех настроек игры

	def __init__(self):
		#Параметры экрана
		self.screen_width = 1200
		self.screen_height = 800
		self.rgb_color = ( 0, 0, 0 )
		#Настройки корабля
		self.ship_speed = 1
		#Параметры выстрелов
		self.bullet_speed = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (255, 0, 0)
		self.bullet_allowed = 3
		#Параметры пауков
