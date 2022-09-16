
import pygame
##################################################################
# 기본 초기화
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 #세로 크기
screen=pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀
pygame.display.set_caption("게임 이름") 
# FPS
clock = pygame.time.Clock()
#######################################################################

#1. 사용자 게임 초기화 (배경화면,게임 이미지,좌표,폰트,속도등)


running = True 
while running:

    #2. 이벤트 처리(키보드,마우스등)
    dt = clock.tick(60) #게임화면의 초당 프레임

    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
        if event.type==pygame.QUIT: #창이 닫히는 이벤트 발생하였는지?
            running=False
       
 
    #3. 게임 캐릭터 위치 정의
     
    
    #4. 충돌처리

    
    #5. 화면에 그리기

 
    pygame.display.update() # 게임 화면 계속 그리기


# pygame 종료
pygame.quit()