# Игра ТЕТЕРИС



# Импорт библиотек
import pygame
import time
import sys
import random



# Активация библиотеки pygame
pygame.init()
pygame.mixer.init()



# Создания класса (Блоков падающих тетрисов)
class CreateBlock():



	# Функция создания блока тетриса типа 2х2(2 на 2)
	def __init__(self):
		# Отрисовка кубиков и в дальнейшем формировка тетрисов(цельных блоков)
		pygame.draw.rect(screen, (255, 255, 0), (random_spawn_block_four_block, y_down, width, heitd))

		pygame.draw.rect(screen, (255, 255, 0), (random_spawn_block_four_block+31, y_down, width, heitd))

		pygame.draw.rect(screen, (255, 255, 0), (random_spawn_block_four_block, y_down+31, width, heitd))

		pygame.draw.rect(screen, (255, 255, 0), (random_spawn_block_four_block+31, y_down+31, width, heitd))


	# Функция создания блока тетриса типа _|_
	def pis_block(self):
		# Отрисовка кубиков и в дальнейшем формировка тетрисов(цельных блоков)
		pygame.draw.rect(screen, (139, 0, 139), (random_spawn_block_pis_block, y_down, width, heitd))

		pygame.draw.rect(screen, (139, 0, 139), (random_spawn_block_pis_block, y_down+31, width, heitd))

		pygame.draw.rect(screen, (139, 0, 139), (random_spawn_block_pis_block+31, y_down+31, width, heitd))

		pygame.draw.rect(screen, (139, 0, 139), (random_spawn_block_pis_block, y_down+62, width, heitd))




# Создание переменных
# Перменная для Вечного Цикла
runing = True


# Указываем раззмеры блоков
width = heitd = 30


# Переменная указывает, какой растояние нужно пропускать между блоков
margin = 1


# Координата "у" для блоков, и для их падения
y_down = 0


# Выбираем рандом спавн падающих блоков (по оси Х) (Для блока тетриса 2х2)
random_spawn_block_four_block = random.choice([283, 314, 345, 376, 407, 438])


# Выбираем рандом спавн падающих блоков (По оси Х) (Для блока тетриса _|_)
random_spawn_block_pis_block = random.choice([283, 314, 345, 376, 407, 438])


# Указываем фпс для нашего цикла
clock = pygame.time.Clock()




# Создание экрана игры
screen = pygame.display.set_mode((750,620))
pygame.display.set_caption("TETRIS")



# Создание вечного цикла
while runing:


	# Обработка пола центральной карты (дабы блоки не проваливались через мир) Если, что крайний y=558 корд.
	# Бета версия обработки поадения блоков(Не правильно функционирует с блоком типа _|_
	if y_down==558:

		y_down=558

	elif y_down==527:

		y_down==527

	elif y_down<558:

		y_down = y_down + 31


	# Указываем цвет фона
	screen.fill((0, 128, 255))


	# Вывод корд. для разраба
	print(y_down)



	# Обработка закрытия окна игры
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			runing = False
			pygame.quit()


	# Создание правого не игрового блока(для отражения информации)
	for col in range(7):
		for row in range(29):
			x = col*width+(col+1)*margin
			y = row*heitd+(row+1)*margin
			pygame.draw.rect(screen,(255,0,0), (x,y,width,heitd))


	# Левое не игровое поле(для отображения онформации)
	for col1 in range(7):
		for row1 in range(29):
			x = col1*width+(col1+1)*margin+533
			y = row1*heitd+(row1+1)*margin+0
			pygame.draw.rect(screen,(255,0,0), (x,y,width,heitd))


	# Создание блоков (главного поля где падают кубики)
	for col2 in range(10):
		for row2 in range(20):
			x = col2*width+(col2+1)*margin+220
			y = row2*heitd+(row2+1)*margin+0
			pygame.draw.rect(screen,(0,191,255), (x,y,width,heitd))



	# Создание надписи
	# TETRIS
	fontTET = pygame.font.Font('PressStart2P-Regular.ttf', 30)
	text_tet = fontTET.render('TETRIS', False, (255,255,255))
	screen.blit(text_tet, (20, 20))


	# Создание надписи
	# Надпись Легендарня 8 битная игра сделанная в СССР
	fontCRT = pygame.font.Font('PressStart2P-Regular.ttf', 7)
	text_tet_CRT = fontCRT.render('Легендарная 8-ми битная игра.', False, (255,255,255))
	screen.blit(text_tet_CRT, (10, 50))


	# Создания класса с функцией __init__ для создания блока тетриса 2х2
	createblock = CreateBlock()


	# Вызов функции для создания блока типа _|_. Вызов происходит из класса CreateBlock().
	createblock.pis_block()


	# Ограничение кадров игры
	clock.tick(3)


	# Обновление экрана
	pygame.display.update()





	
