# Импорт библиотек
import pygame
import time
import sys


# Создание переменных
runing = True

# Активация библиотеки pygame
pygame.init()
pygame.mixer.init()

# Создание экрана игры
screen = pygame.display.set_mode((600,900))
pygame.display.set_caption("TETRIS")


# Создание вечного цикла
while runing:
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			runing = False
			pygame.quit()



	
