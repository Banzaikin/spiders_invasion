import pygame
import time
import os

class Music():
	#Класс для управления музыкой

	def __init__(self):
		#Инициализирует музыку
		pygame.mixer.init()
		os.add_dll_directory('C:/Users/trajt/AppData/Local/Packages' +
			'/PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0/LocalCache' +
			'/local-packages/Python310/site-packages/pygame')
		self.playlist()
		self.playing_music()
	
	def playlist(self):
		#Создание плейлиста
		self.playlist = []
		self.playlist.append ('sounds/dinamicnaa_muzyka_vostocnaa.mp3')
		self.playlist.append ('sounds/etniceskaa_slavanskaa_muzyka.mp3')
		self.playlist.append ('sounds/tehnika_dinamicnaa_muzyka.mp3')
		self.playlist.append ('sounds/boevaa_muzyka_razrusenie_planety.mp3')
		self.playlist.append ('sounds/dinamicnaa_muzyka_dinamicnaa.mp3')

	def playing_music(self):
		#Воспроизведение плейлиста
		self.trek = self.playlist.pop()
		self.playlist.append(self.trek)
		pygame.mixer.music.load (self.trek)  
		pygame.mixer.music.queue (self.playlist.pop()) 
		pygame.mixer.music.set_endevent (pygame.USEREVENT)    
		pygame.mixer.music.play()   

		
