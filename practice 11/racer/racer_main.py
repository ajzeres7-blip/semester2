import pygame
import random
import time

pygame.init()

#screen settings
WIDTH=400
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
#load images
image_background=pygame.image.load('resources/AnimatedStreet.png')
image_player=pygame.image.load('resources/Player.png')
image_enemy=pygame.image.load('resources/Enemy.png')
#sounds loading
pygame.mixer.music.load('resources/background.wav')
pygame.mixer.music.play(-1)

sound_crash=pygame.mixer.Sound('resources/crash.wav')
#font
font=pygame.font.SysFont('Verdana',60)
image_game_over=font.render("Game Over", True, "black")
image_game_over_rect=image_game_over.get_rect(center=(WIDTH//2, HEIGHT//2))

#Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=image_player
        self.rect=self.image.get_rect()
        self.rect.centerx=WIDTH//2
        self.rect.bottom=HEIGHT
        self.speed=5
    def move(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed,0)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed,0)
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.right>WIDTH:
            self.rect.right=WIDTH

#Enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=image_enemy
        self.rect=self.image.get_rect()
        self.speed=6 #starting speed
    def generate_random_rect(self):
        self.rect.left=random.randint(0, WIDTH-self.rect.w)
        self.rect.bottom=0
    def move(self):
         self.rect.move_ip(0,self.speed)
         #respawn when off screen
         if self.rect.top>HEIGHT:
             self.generate_random_rect()
#Coin
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size=20
        self.image=pygame.Surface((self.size, self.size))
        self.rect=self.image.get_rect()
        self.speed=5
        self.randomize_type()
        self.generate_random_rect()
    def randomize_type(self):
        #random weight type
        self.weight=random.choice([1,2,3])
        #assign color based on weight
        if self.weight==1:
            self.color=(255,215,0) #gold
        elif self.weight==2:
            self.color=(0,191,255) #blue
        else:
            self.color=(255,0,255) #purple
        self.image.fill(self.color)
    def generate_random_rect(self):
        self.randomize_type()
        #Spawn randomly on road
        self.rect.left=random.randint(0, WIDTH-self.size)
        self.rect.bottom=0
    def move(self):
        self.rect.move_ip(0,self.speed)
        #respawn if missed
        if self.rect.top>HEIGHT:
            self.generate_random_rect()
#game setup
running=True
clock=pygame.time.Clock()
FPS=60
player=Player()
enemy=Enemy()
coin=Coin()
all_sprites=pygame.sprite.Group()
enemy_sprites=pygame.sprite.Group()
coin_sprites=pygame.sprite.Group()
all_sprites.add(player,enemy,coin)
enemy_sprites.add(enemy)
coin_sprites.add(coin)

#coin variables
score=0
coins_collected=0
LEVEL_UP_COINS=5 #every 5 coins collected increases level

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    #move player & draw background
    player.move()
    screen.blit(image_background, (0,0))
    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)
    #coin collision
    if pygame.sprite.spritecollideany(player, coin_sprites):
        score+=coin.weight #add based on weight
        coins_collected+=1
        coin.generate_random_rect() #respawn coin
    #enemy collision
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        sound_crash.play()
        time.sleep(1)

        running=False
        screen.fill("red")
        screen.blit(image_game_over, image_game_over_rect)
        pygame.display.flip()
        time.sleep(3)
    #UI
    score_text=font.render(f'Score:{score}', True, 'black')
    speed_text=font.render(f'Enemy Speed: {enemy.speed}', True, 'black')
    screen.blit(score_text, (10,10))
    screen.blit(speed_text, (10,40))
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()