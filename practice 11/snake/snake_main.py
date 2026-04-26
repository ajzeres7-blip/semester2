import pygame
import sys
import random
pygame.init()
#screen settings
WIDTH, HEIGHT =600, 400
CELL_SIZE=20
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock =pygame.time.Clock()
#colors
BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,200,0)
RED=(200,0,0)
BLUE=(0,0,255)
GOLD=(255,215,0)
font=pygame.font.SysFont("Verdana", 24)
#snake initial state
snake=[(100,100), (80, 100), (60,100)]
direction =(CELL_SIZE, 0)
#game  stats
score=0
level=1
foods_to_next_level=3
speed=5
#generate food with random weight and timer
def generate_food():
    while True:
        x=random.randint(0,(WIDTH-CELL_SIZE)//CELL_SIZE)*CELL_SIZE
        y=random.randint(0,(HEIGHT-CELL_SIZE)//CELL_SIZE)*CELL_SIZE
        if (x,y) not in snake:
            food_type=random.choice([1,2,3])
            if food_type==1:
                return {
                    'pos':(x,y),
                    'weight': 1,
                    'color' :RED,
                    'lifetime':7000, #milliseconds
                    'spawn_time': pygame.time.get_ticks()
                }
            elif food_type==2:
                return {
                    'pos':(x,y),
                    'weight':2,
                    'color': BLUE,
                    'lifetime':5000,
                    'spawn_time':pygame.time.get_ticks()
                    }
            else:
                return {
                    'pos': (x,y),
                    'weight':3,
                    'color':GOLD,
                    'lifetime':3000,
                    'spawn_time':pygame.time.get_ticks()
                }
food=generate_food()

def draw_snake():
    for block in snake:
        pygame.draw.rect(screen, GREEN, (block[0], block[1], CELL_SIZE, CELL_SIZE))

def draw_food():
    pygame.draw.rect(screen, food['color'], (food['pos'][0], food['pos'][1], CELL_SIZE, CELL_SIZE))

def check_wall_collision(head):
    if head[0]<0 or head[0]>=WIDTH or head[1]<0 or head[1]>=HEIGHT:
        return True
    return False
def check_self_collision(head):
    if head in snake[1:]:
        return True
    return False
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        #movement controls
        if  event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP and direction!=(0,CELL_SIZE):
                direction=(0, -CELL_SIZE)
            elif event.key==pygame.K_DOWN and direction!=(0, -CELL_SIZE):
                direction=(0, CELL_SIZE)
            elif event.key==pygame.K_LEFT and direction!=(CELL_SIZE,0):
                direction=(-CELL_SIZE,0)
            elif event.key==pygame.K_RIGHT and direction!=(-CELL_SIZE, 0):
                direction=(CELL_SIZE, 0)
    #move snake
    head_x, head_y=snake[0]
    new_head=(head_x+direction[0], head_y+direction[1])
    #collision checks
    if check_wall_collision(new_head):
        print("Game Over: Wall Collision")
        pygame.quit()
        sys.exit()
    if check_self_collision(new_head):
        print("Game Over: Self Collision")
        pygame.quit()
        sys.exit()
    snake.insert(0, new_head)
    #check eaten food
    if new_head==food['pos']:
        score+=food['weight']
        foods_to_next_level-=1
        food=generate_food()
    else:
        snake.pop()
    #food timer-disappearment
    current_time=pygame.time.get_ticks()
    if current_time-food['spawn_time']>food['lifetime']:
        food=generate_food() #replace food if expired
    #level system
    if foods_to_next_level==0:
        level+=1
        foods_to_next_level=3
        speed+=2
    #drawing
    screen.fill(BLACK)
    draw_snake()
    draw_food()
    #UI text
    score_text=font.render(f"Score:{score}", True, WHITE)
    screen.blit(score_text, (10,10))
    level_text=font.render(f"Level:{level}", True, WHITE)
    screen.blit(level_text, (10,40))
    
    pygame.display.update()
    clock.tick(speed)