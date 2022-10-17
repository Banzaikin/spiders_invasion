import pickle

class GameStats():
	#Статистика игры

	def __init__(self, ai_game):
		#Инициализирует статистику
		self.settings = ai_game.settings
		self.reset_stats()
		#Игра запускается в неактивном состоянии
		self.game_active = False
		#Рекорд не должен сбрасываться после выключения игры
		self.high_score = 0
		
	def reset_stats(self):
		#Инициализирует статистику, изменяющуюся в ходе игры
		self.ships = self.settings.ships_limit
		self.level = 1
		self.score = 0
		try:
			with open('score.dat', 'rb') as file:
				self.score = pickle.load(file)
		except:
			self.score = 0
		with open('score.dat', 'wb') as file:
			pickle.dump(self.score, file)