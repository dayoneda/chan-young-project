#from ast import Pass
#from curses import KEY_RIGHT
#from cProfile import run

import random
from secrets import randbits
import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 #세로 크기
screen=pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀
pygame.display.set_caption("chanyoung Game") # 게임 이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기 
background = pygame.image.load("C:/Users/cksdu/Desktop/python/pygame_basic/background.png")

# 캐릭터(스프라이트) 불러오기
character=pygame.image.load("C:/Users/cksdu/Desktop/python/pygame_basic/character.png")
character_size=character.get_rect().size # 이미지의 크기를 구해옴
character_width=character_size[0] #캐릭터 가로 크기
character_height=character_size[1] #캐릭터 세로 크기
character_x_pos=(screen_width /2)- (character_width / 2.4) #화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos=screen_height-character_height #화면 세로크기 가장 아래

# 적 (enemy) 캐릭터 불러오기
enemy=pygame.image.load("C:/Users/cksdu/Desktop/python/pygame_basic/enemy.png")
enemy_size=enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width=enemy_size[0] #캐릭터 가로 크기
enemy_height=enemy_size[1] #캐릭터 세로 크기
enemy_x_pos=random.randint(0,screen_width-enemy_width) 
enemy_y_pos=0 




# 이동할 좌표
to_x = 0
to_y = 0

# 이동속도 
character_speed=0.6

#폰트 정의
game_font=pygame.font.Font(None,40) #폰트 객체 생성 (폰트,크기)

#총 시간
total_time=30

#시작시간
start_ticks=pygame.time.get_ticks() #시작 tick을 받아옴


#이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) #게임화면의 초당 프레임
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
        if event.type==pygame.QUIT: #창이 닫히는 이벤트 발생하였는지?
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                to_x -= character_speed
            elif event.key==pygame.K_RIGHT:
                to_x += character_speed
            elif event.key==pygame.K_UP:
                to_y -= character_speed
            elif event.key==pygame.K_DOWN:
                to_y += character_speed
 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == event.key ==pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == event.key ==pygame.K_DOWN:    
                to_y = 0
    
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
    
    # 가로 경계값 처리
    if character_x_pos <0:
        character_x_pos=0
    elif character_x_pos>screen_width-character_width:
        character_x_pos=screen_width-character_width
    # 세로 경계값 처리
    if character_y_pos <0:
        character_y_pos=0
    elif character_y_pos>screen_height-character_height:
        character_y_pos=screen_height-character_height

    enemy_y_pos+=20
    if enemy_y_pos > screen_height:
        enemy_x_pos=random.randint(0,screen_width-enemy_width) 
        enemy_y_pos=0 
        
    # 충돌처리(rect 정보 업데이트)
    character_rect=character.get_rect()
    character_rect.left=character_x_pos
    character_rect.top=character_y_pos
    
    enemy_rect=enemy.get_rect()
    enemy_rect.left=enemy_x_pos
    enemy_rect.top=enemy_y_pos

    #충돌체크
    if character_rect.colliderect(enemy_rect):
        print("충돌하였습니다!")
        running=False

    screen.blit(background, (0,0)) #배경 그리기

    screen.blit(character,(character_x_pos,character_y_pos)) # 캐릭터 그리기

    screen.blit(enemy,(enemy_x_pos,enemy_y_pos)) # 적 그리기

    #타이머 집어 넣기 (경과 시간 계산)
    elapsed_time=(pygame.time.get_ticks()-start_ticks)/1000
    timer=game_font.render(str(int(total_time-elapsed_time)),True,(255,255,255))
    screen.blit(timer,(10,10))
    # 시간이 0초이하면 게임종료
    if total_time-elapsed_time <=0:
        print("성공!")
        running =False
    pygame.display.update() # 게임 화면 계속 그리기

#잠시 대기
pygame.time.delay(1000)

# pygame 종료
pygame.quit()