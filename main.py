import pygame
import random
import math
#initialization
pygame.init() 



screen = pygame.display.set_mode((800, 600))
#background

background = pygame.image.load('ss.jpg')

pygame.display.set_caption("space invaders") 
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)


#player
playerImage = pygame.image.load("game.png")
playerX = 370
playerY = 480
playerX_change = 0
playerX_change = 0


# enemy 
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemy = 6
for i in range(num_of_enemy):
    enemyImg.append(pygame.image.load("skull.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)
    bullet_state = "ready"


#bullet

#ready = you cant see the bullet on screen
#fire = the bullet is currently moving
bulletImage = pygame.image.load("bul.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10

score =0
font =  pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

def show_score(x, y):
    score_v = font.render("Score: " + str(score), True, (255, 255, 255))
    
def player(x, y):
    screen.blit(playerImage, (x, y))  #blit means to draw




def enemy(x, y,i):
    screen.blit(enemyImg[i], (x, y))  #blit means to draw




def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImage,(x+16,y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2))+( math.pow(enemyY-bulletY, 2)))
                                 
    if distance <27:
        return True
    else:
        return False
running = True 
while running:
    screen.fill((0,0,0))

    screen.blit(background, (0,0))


    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3

            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3

            if event.key == pygame.K_SPACE:  
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
 # enemy movement

    for i in range(num_of_enemy):

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]


            # collision
        Collision = isCollision(enemyX, enemyY, bulletX, bulletY)
        if Collision:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            print(score)
            enemyX = random.randint(0, 735)
            enemyY = random.randint(50, 150)

        enemy(enemyX[i],enemyY[i],i)
    
#bullete movement
        
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
# collision
    Collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if Collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)
        
    player(playerX, playerY)
    pygame.display.update()


