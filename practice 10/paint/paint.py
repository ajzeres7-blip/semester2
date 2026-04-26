import pygame
import sys
pygame.init()
#Screen
WIDTH, HEIGHT=800,600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Paint App")
#Colors
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)

colors=[BLACK,RED,BLUE,GREEN]
current_color=BLACK
#Tools
tool='brush'
clock=pygame.time.Clock()
drawing=False
start_pos=None
screen.fill(WHITE)
def draw_ui():
    #Draw color pallete
    for i, col in enumerate(colors):
        pygame.draw.rect(screen,col,(10+i*40, 10,30,30))
    #Draw tool labels
    font=pygame.font.SysFont(None,24)
    tools=['brush', 'rect', 'circle', 'eraser']
    for i, t in enumerate(tools):
        text=font.render(t, True, BLACK)
        screen.blit(text,(10+i*80, 50))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        #Mouse down
        if event.type==pygame.MOUSEBUTTONDOWN:
            drawing=True
            start_pos=event.pos

            x,y=event.pos
            #Check color selection
            for i, col in enumerate(colors):
                if 10+i*40<=x<=40+i*40 and 10<=y<=40:
                    current_color=col
        #Tool selection (keys)
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_b:
                tool='brush'
            elif event.key==pygame.K_r:
                tool='rect'
            elif event.key==pygame.K_c:
                tool='circle'
            elif event.key==pygame.K_e:
                tool='eraser'
        #Mouse up
        if event.type==pygame.MOUSEBUTTONUP:
            drawing=False
            end_pos=event.pos
            if tool=='rect':
                rect=pygame.Rect(start_pos,(end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
                pygame.draw.rect(screen,current_color,rect,2)
            elif tool=='circle':
                radius=int(((end_pos[0]-start_pos[0])**2+(end_pos[1]-start_pos[1])**2)**0.5)
                pygame.draw.circle(screen,current_color, start_pos, radius, 2)
    #Drawing while moving
    if drawing:
        mouse_pos=pygame.mouse.get_pos()
        if tool=='brush':
            pygame.draw.circle(screen, current_color, mouse_pos, 5)
        elif tool=='eraser':
            pygame.draw.circle(screen, WHITE, mouse_pos,10)
    draw_ui()
    pygame.display.flip()
    clock.tick(60)

