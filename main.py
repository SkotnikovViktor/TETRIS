# Импорт библиотек
import pygame
import time
import sys
import random



# Создания класса (Блоков падающих тетрисов)
class CreateBlock():

	# Создания тетрис блока (2х2) (кубик)
	def __init__(self):
		pygame.draw.rect(screen, (255, 255, 0), (random_spawn_block_four_block, y_down, width, heitd))
		pygame.draw.rect(screen, (255, 255, 0), (random_spawn_block_four_block+31, y_down, width, heitd))
		pygame.draw.rect(screen, (255, 255, 0), (random_spawn_block_four_block, y_down+31, width, heitd))
		pygame.draw.rect(screen, (255, 255, 0), (random_spawn_block_four_block+31, y_down+31, width, heitd))



	def pis_block(self):
		pygame.draw.rect(screen, (139, 0, 139), (random_spawn_block_pis_block, y_down, width, heitd))
		pygame.draw.rect(screen, (139, 0, 139), (random_spawn_block_pis_block, y_down+31, width, heitd))
		pygame.draw.rect(screen, (139, 0, 139), (random_spawn_block_pis_block+31, y_down+31, width, heitd))
		pygame.draw.rect(screen, (139, 0, 139), (random_spawn_block_pis_block, y_down+62, width, heitd))





# Создание переменных
runing = True
width = heitd = 30
margin = 1
y_down = 0
#random_spawn_block = random.choice([283,314,345,376,407,438])
clock = pygame.time.Clock()
random_spawn_block_four_block = random.choice([283, 314, 345, 376, 407, 438])
random_spawn_block_pis_block = random.choice([283, 314, 345, 376, 407, 438])



# Активация библиотеки pygame
pygame.init()
pygame.mixer.init()

# Создание экрана игры
screen = pygame.display.set_mode((750,620))
pygame.display.set_caption("TETRIS")





# Создание квадратов (по бокам) Номер блока: 1
#suqre = pygame.Surface((550,950))
# Цвет блока
#suqre.fill((0,0,0))

#suqre2 = pygame.Surface((550,950))
# Цвет блока
#suqre2.fill((0,0,0))

#world = pygame.Surface((500,100))
#world.fill((51,51,0))

# Создание вечного цикла
while runing:


	# Обработка пола центральной карты (дабы блоки не проваливались через мир) Если, что крайний y=558 корд.
	if y_down==558:
		y_down=558
	elif y_down==527:
		y_down==527
	elif y_down<558:
		y_down = y_down + 31


	# Указываем цвет фона
	screen.fill((0, 128, 255))

	print(y_down)


	#for i in range(10000):
	#	color_text_tet = random.randint(0, 255)
	#	color_text_tet2 = random.randint(0, 255)
	#	color_text_tet3 = random.randint(0, 255)



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



	# Создание текста TETRIS
	fontTET = pygame.font.Font('PressStart2P-Regular.ttf', 30)
	text_tet = fontTET.render('TETRIS', False, (255,255,255))
	screen.blit(text_tet, (20, 20))


	# Надпись Легендарня 8 битная игра сделанная в СССР
	fontCRT = pygame.font.Font('PressStart2P-Regular.ttf', 7)
	text_tet_CRT = fontCRT.render('Легендарная 8-ми битная игра.', False, (255,255,255))
	screen.blit(text_tet_CRT, (10, 50))

	createblock = CreateBlock()
	#createblock.pis_block()
	# Обновление экрана
	pygame.display.update()

	# Ограничение кадров игры
	clock.tick(3)



	
