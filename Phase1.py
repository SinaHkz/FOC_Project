def R_fun(board):
    for j in range(n-1,0,-1):
        for i in range(n):
            if board[i][j]==0:
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
            if board[i][j]==0:
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
            if board[i][j]==0:
                board[i][j],board[i-1][j]=(board[i-1][j],board[i][j])
            else:
                if board[i][j]==1 and board[i-1][j]==2:
                    board[i][j]=3
                    board[i-1][j]=0
                elif board[i][j]==2 and board[i-1][j]:
                    board[i][j]=3
                    board[i-1][j]=0
                elif board[i][j]!=1 and board[i][j]!=2 and board[i][j]==board[i-1][j]:
                    board[i][j]=2*(board[i][j])
                    board[i-1][j]=0
    return board

def D_fun(board):
    for i in range(n-1,0,-1):
        for j in range(n):
            if board[i][j]==0:
                board[i][j],board[i+1][j]=(board[i+1][j],board[i][j])
            else:
                if board[i][j]==1 and board[i+1][j]==2:
                    board[i][j]=3
                    board[i+1][j]=0
                elif board[i][j]==2 and board[i+1][j]:
                    board[i][j]=3
                    board[i+1][j]=0
                elif board[i][j]!=1 and board[i][j]!=2 and board[i][j]==board[i+1][j]:
                    board[i][j]=2*(board[i][j])
                    board[i+1][j]=0
    return board           

def randomPlace(board,k):
    count1 = []
    count2 = []
    for i in range(n):
        for j in range(n):
            if board[i][j]==0:
                count1+=[j]
                count2+=[i]
                break
    m1 = len(set(count1))
    m2 = len(set(count2))
    j = k%m1
    i = k%m2
    list = [i , j]
    return list


n = int(input())
board = []
for i in range(n):
    inp = input().split()
    for j in range(n):
        inp[j]=int(inp[j])
    board+=[inp]

way = input()
for q in way:
    flaq = True
    if q=='R':
        if board==R_fun(board):
            flaq = False
        board = R_fun(board)
    elif q=='L':
        if board==L_fun(board):
            flaq = False
        board = L_fun(board)
    elif q=='U':
        if board==U_fun(board):
            flaq = False
        board = U_fun(board)
    elif q=='D':
        if board==D_fun(board):
            flaq = False
        board = D_fun(board)
    move = input().split()
    if flaq :
        for i in range(len(move)):
            move[i]=int(move[i])
        list = randomPlace(board,move[1])
        board[list[0]][list[1]]=move[0]
print(board)