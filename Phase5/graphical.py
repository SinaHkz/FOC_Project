import pygame , time, sys
import random
from pygame.locals import *

threes = [[0]*4 for i in range(4)]
# this part make a random board.
for i in range(9):
    r,c = random.randint(0,3),random.randint(0,3)
    while threes[r][c]!=0:
        r,c = random.randint(0,3),random.randint(0,3)
    threes[r][c] = random.randint(1,3)


def copy(board):
    test = []
    for i in range(n):
        help = []
        for j in range(n):
            help+=[board[i][j]]
        test += [help]
    return test


def R_fun(board):
    for j in range(n-1,0,-1):
        for i in range(n):
            if board[i][j]==0 or board[i][j]=="":
                board[i][j],board[i][j-1]=(board[i][j-1],board[i][j])
            else:
                if board[i][j]==1 and board[i][j-1]==2:
                    board[i][j]=3
                    board[i][j-1]=0
                elif board[i][j]==2 and board[i][j-1]==1:
                    board[i][j]=3
                    board[i][j-1]=0
                elif board[i][j]!=1 and board[i][j]!=2 and board[i][j]==board[i][j-1]:
                    board[i][j]=2*(board[i][j])
                    board[i][j-1]=0
    return board

def L_fun(board):
    for j in range(0,n-1,):
        for i in range(n):
            if board[i][j]==0 or board[i][j]=="":
                board[i][j],board[i][j+1]=(board[i][j+1],board[i][j])
            else:
                if board[i][j]==1 and board[i][j+1]==2:
                    board[i][j]=3
                    board[i][j+1]=0
                elif board[i][j]==2 and board[i][j+1]==1:
                    board[i][j]=3
                    board[i][j+1]=0
                elif board[i][j]!=1 and board[i][j]!=2 and board[i][j]==board[i][j+1]:
                    board[i][j]=2*(board[i][j])
                    board[i][j+1]=0
    return board

def U_fun(board):
    for i in range(0,n-1):
        for j in range(n):
            if board[i][j]==0 or board[i][j]=="":
                board[i][j],board[i+1][j]=(board[i+1][j],board[i][j])
            else:
                if board[i][j]==1 and board[i+1][j]==2:
                    board[i][j]=3
                    board[i+1][j]=0
                elif board[i][j]==2 and board[i+1][j]==1:
                    board[i][j]=3
                    board[i+1][j]=0
                elif board[i][j]!=1 and board[i][j]!=2 and board[i][j]==board[i+1][j]:
                    board[i][j]=2*(board[i][j])
                    board[i+1][j]=0
    return board

def D_fun(board):
    for i in range(n-1,0,-1):
        for j in range(n):
            if board[i][j]==0 or board[i][j]=="":
                board[i][j],board[i-1][j]=(board[i-1][j],board[i][j])
            else:
                if board[i][j]==1 and board[i-1][j]==2:
                    board[i][j]=3
                    board[i-1][j]=0
                elif board[i][j]==2 and board[i-1][j]==1:
                    board[i][j]=3
                    board[i-1][j]=0
                elif board[i][j]!=1 and board[i][j]!=2 and board[i][j]==board[i-1][j]:
                    board[i][j]=2*(board[i][j])
                    board[i-1][j]=0
    return board    
def is_done(board):
    test = copy(board)
    test1 = R_fun(copy(board))
    test2 = L_fun(copy(board))
    test3 = U_fun(copy(board))
    test4 = D_fun(copy(board))
    if test1==test and test2==test and test3==test and test4==test:
        return True
    return False
    
    
numList = [1, 1, 1, 2, 2, 2, 2, 3]
def randomPlace_R(board):
        dict = {}
        count = 0
        for i in range(4):
            if board[i][0]==0 or board[i][0]=="":
                dict[count]=i
                count+=1
        a = list(dict.keys())
        x = random.choice(a)
        board[dict[x]][0]=random.choice(numList)
def randomPlace_L(board):
        dict = {}
        count = 0
        for i in range(4):
            if board[i][3]==0 or board[i][3]=="":
                dict[count]=i
                count+=1
        a = list(dict.keys())
        x = random.choice(a)
        board[dict[x]][3]=random.choice(numList)
def randomPlace_U(board):
        dict = {}
        count = 0
        for j in range(n):
            if board[3][j]==0 or board[3][j]=="":
                dict[count]=j
                count+=1
        a = list(dict.keys())
        x = random.choice(a)
        board[3][dict[x]]=random.choice(numList)
def randomPlace_D(board):
        dict = {}
        count = 0
        for j in range(n):
            if board[0][j]==0 or board[0][j]=="":
                dict[count]=j
                count+=1
        a = list(dict.keys())
        x = random.choice(a)
        board[0][dict[x]]=random.choice(numList)

pygame.init()
blue = (100,200,255)

#diplay setting
win = pygame.display.set_mode((700,700))
pygame.display.set_caption("Threes")
win.fill(blue)

#img = pygame.image.load("/Users/sina/Desktop/FOC_Project/Phase5/a.svg.png")
#pygame.display.set_icon(img)

#this two parts are about icon of the game.


a0 = str(threes[0][0])
a1 = str(threes[0][1])
a2 = str(threes[0][2])
a3 = str(threes[0][3])
b0 = str(threes[1][0])
b1 = str(threes[1][1])
b2 = str(threes[1][2])
b3 = str(threes[1][3])
c0 = str(threes[2][0])
c1 = str(threes[2][1])
c2 = str(threes[2][2])
c3 = str(threes[2][3])
d0 = str(threes[3][0])
d1 = str(threes[3][1])
d2 = str(threes[3][2])
d3 = str(threes[3][3])


#a lot of these function copied from phases 1 to 3 and because of different cols and rows that their board have we have n instead 4 and this is just for amking sure the code is running well.
n = 4


#infinit loop to keep the diplay of game on.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        #functions of each key.  
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if L_fun(copy(threes))!=threes:
                    L_fun(threes)
                    randomPlace_L(threes)
                
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                if R_fun(copy(threes))!=threes:
                    R_fun(threes)
                    randomPlace_R(threes)
                
        if event.type == KEYDOWN:
            if event.key == K_UP:
                if U_fun(copy(threes))!=threes:
                    U_fun(threes)
                    randomPlace_U(threes)
                
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                if D_fun(copy(threes))!=threes:
                    D_fun(threes)
                    randomPlace_D(threes)
                
    #board sizes.      
    pygame.draw.rect(win , (50,50,50), (50,50 ,600,600))
    pygame.draw.line(win , (255,255,255), (200,50), (200,650))
    pygame.draw.line(win , (255,255,255), (350,50), (350,650))
    pygame.draw.line(win , (255,255,255), (500,50), (500,650))
    pygame.draw.line(win , (255,255,255), (50,200), (650,200))
    pygame.draw.line(win , (255,255,255), (50,350), (650,350))
    pygame.draw.line(win , (255,255,255), (50,500), (650,500))
    for i in range(4):
        for j in range(4):
            if threes[i][j]==0:
                threes[i][j]=""
    a0 = str(threes[0][0])
    a1 = str(threes[0][1])
    a2 = str(threes[0][2])
    a3 = str(threes[0][3])
    b0 = str(threes[1][0])
    b1 = str(threes[1][1])
    b2 = str(threes[1][2])
    b3 = str(threes[1][3])
    c0 = str(threes[2][0])
    c1 = str(threes[2][1])
    c2 = str(threes[2][2])
    c3 = str(threes[2][3])
    d0 = str(threes[3][0])
    d1 = str(threes[3][1])
    d2 = str(threes[3][2])
    d3 = str(threes[3][3])
    
    
    

    #showing the number of each area as a image.
    font = pygame.font.SysFont(None, 100)
    img = font.render(a0, True, (255,255,255))
    win.blit(img, (100,100))

    font2 = pygame.font.SysFont(None, 100)
    img2 = font.render(a1, True, (255,255,255))
    win.blit(img2, (250,100))

    font3 = pygame.font.SysFont(None, 100)
    img3 = font.render(a2, True, (255,255,255))
    win.blit(img3, (400,100))

    font4 = pygame.font.SysFont(None, 100)
    img4 = font.render(a3, True, (255,255,255))
    win.blit(img4, (550,100))

    font5 = pygame.font.SysFont(None, 100)
    img5 = font.render(b0, True, (255,255,255))
    win.blit(img5, (100,250))

    font6 = pygame.font.SysFont(None, 100)
    img6 = font.render(b1, True, (255,255,255))
    win.blit(img6, (250,250))

    font7 = pygame.font.SysFont(None, 100)
    img7 = font.render(b2, True, (255,255,255))
    win.blit(img7, (400,250))

    font8 = pygame.font.SysFont(None, 100)
    img8 = font.render(b3, True, (255,255,255))
    win.blit(img8, (550,250))

    font9 = pygame.font.SysFont(None, 100)
    img9 = font.render(c0, True, (255,255,255))
    win.blit(img9, (100,400))

    font10 = pygame.font.SysFont(None, 100)
    img10 = font.render(c1, True, (255,255,255))
    win.blit(img10, (250,400))

    font11 = pygame.font.SysFont(None, 100)
    img11 = font.render(c2, True, (255,255,255))
    win.blit(img11, (400,400))

    font12 = pygame.font.SysFont(None, 100)
    img12 = font.render(c3, True, (255,255,255))
    win.blit(img12, (550,400))

    font13 = pygame.font.SysFont(None, 100)
    img13 = font.render(d0, True, (255,255,255))
    win.blit(img13, (100,550))

    font14 = pygame.font.SysFont(None, 100)
    img14 = font.render(d1, True, (255,255,255))
    win.blit(img14, (250,550))

    font15 = pygame.font.SysFont(None, 100)
    img15 = font.render(d2, True, (255,255,255))
    win.blit(img15, (400,550))

    font16 = pygame.font.SysFont(None, 100)
    img16 = font.render(d3, True, (255,255,255))
    win.blit(img16, (550,550))
    
    #checking the status of the game.
    if is_done(threes):
        score = 0
        for i in range(n):
            for j in range(n):
                if threes[i][j]!=1 and threes[i][j]!=2 and threes[i][j]!="" and threes[i][j]!=0:
                    num = int(threes[i][j])//3
                    count = 0
                    while num!=1:
                        num = num//2
                        count += 1
                    score+=3**(count+1)
        text = "Game Over"
        text2 = "The final score is " + str(score) + "."
        font = pygame.font.SysFont(None, 100)
        img = font.render(text, True, (255,0,255))
        win.blit(img, (150,150))

        font = pygame.font.SysFont(None, 50)
        img = font.render(text2, True, (255,0,255))
        win.blit(img, (170,320))
    
    
    pygame.display.update()
