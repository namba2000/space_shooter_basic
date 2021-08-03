import pygame
import random
pygame.init()

# màu

w = (255, 255, 255)
b = (0, 0, 0)
r = (213, 50, 80)


height_scrn = 600
width_scrn = 600
screen = pygame.display.set_mode((width_scrn, height_scrn))
pygame.display.set_caption("Space Shooter")
running = True
pausing = False
clock = pygame.time.Clock()
score = 0
font = pygame.font.SysFont('san' ,30)
font1 = pygame.font.SysFont('san' ,60)

# tốc độ
x_velocity = 5
y_velocity = 4

# hình nền
bg_x = 150
bg_y = 0
bg = pygame.image.load('bg.png')

# tàu
ship_x = 200
ship_y = 500
ship_x_velocity = 20
ship = pygame.image.load('ship.png')
# đạn 
bullet_x = ship_x + 25
bullet_y = 500
bullet_y_velocity = 10
bullet = pygame.image.load('bullet.png')
# tàu quái vật 
blood_monster = 200
ship_monster_x = 180 + 250
ship_monster_y = bg_y
ship_monster_x_velocity = random.randint(2,3)
ship_monster = pygame.image.load('ship_monster.png')
# đạn quái vật
bullet_monster_x = ship_monster_x + 35
bullet_monster_y = 40
bullet_monster_y_velocity = 5
bullet_monster = pygame.image.load('bullet_monster.png')
bullet_monster_y_velocity = 5

while running:
	clock.tick(60)
	screen.fill(w)
	# màn hình điểm và máu quái vật
	score_text = font1.render("Score", True, b)
	screen.blit(score_text, (18,70))
	score_text_1 = font1.render("" + str(score), True, b)
	screen.blit(score_text_1, (65,140))
	blood_monster_text = font.render("Hp_monster", True, b)
	screen.blit(blood_monster_text, (20,230))
	blood_monster_text1 = font.render("" + str(blood_monster), True, b)
	screen.blit(blood_monster_text1, (65,270))
	notification = font.render("How to play", True, b)
	screen.blit(notification, (2,350))
	notification = font.render("Press left", True, b)
	screen.blit(notification, (12,390))
	notification = font.render("or right", True, b)
	screen.blit(notification, (12,420))

	# màn hình cho background
	bg_rect_1 = screen.blit(bg, (bg_x, bg_y))
	bg_rect_2 = screen.blit(bg, (bg_x, bg_y - 600)) # background 2 nối tiếp background 1
	# chuyển cảnh background
	bg_y = bg_y + y_velocity 
	if bg_y - 600 >= 0:
		bg_y = 0

    # màn hình cho tàu
	ship_rect = screen.blit(ship, (ship_x, ship_y))

	# màn hình cho đạn
	bullet_rect = screen.blit(bullet, (bullet_x, bullet_y))
	bullet_y -= bullet_y_velocity
	if bullet_y <= 0:
		bullet_y = 500

	# màn hình cho tàu quái vật
	ship_monster_rect = screen.blit(ship_monster, (ship_monster_x, ship_monster_y))

	# màn hình cho đạn quái vật
	bullet_monster_rect = screen.blit(bullet_monster, (bullet_monster_x, bullet_monster_y))
	bullet_monster_y += bullet_monster_y_velocity
	if bullet_monster_y > height_scrn:
		bullet_monster_y = 40

	# # tàu người chơi trúng đạn
	if ship_rect.colliderect(bullet_monster_rect):
		pausing = True
		x_velocity = 0
		y_velocity = 0
		bullet_monster_y_velocity = 0
		bullet_y_velocity = 0

	# tàu quái vật trúng đạn
	if ship_monster_rect.colliderect(bullet_rect):
		blood_monster -= 1
		bullet_y = 500
		score += 1
		if blood_monster % 2 != 0:
			ship_monster_x *= ship_monster_x_velocity
			# hết biên
			if ship_monster_x > 480:
				ship_monster_x /= ship_monster_x_velocity
				bullet_monster_x /= ship_monster_x_velocity
		else:
			ship_monster_x /= ship_monster_x_velocity
			# hết biên
			if ship_monster_x <= 150:
				ship_monster_x *= ship_monster_x_velocity
				bullet_monster_x *= ship_monster_x_velocity

	# tàu quái vật hết máu
	if blood_monster == 0:
			y_velocity = 0
			bullet_monster_y_velocity = 0
			bullet_y_velocity = 0
			gameover_text = font.render("You win", True, r)
			screen.blit(gameover_text, (30,200))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			# hoạt động của tàu
			## sang trái 
			if event.key == pygame.K_LEFT:
				ship_x -= ship_x_velocity
				bullet_x -= ship_x_velocity
				# hết biên
				if ship_x <= 150:
					ship_x += ship_x_velocity
					bullet_x += ship_x_velocity
			## sang phải
			if event.key == pygame.K_RIGHT:
				ship_x += ship_x_velocity
				bullet_x += ship_x_velocity
				# hết biên
				if ship_x >= 600 - 80:
					ship_x -= ship_x_velocity
					bullet_x -= ship_x_velocity


	pygame.display.flip()
pygame.quit()
