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
            if board[i][j]==0:
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

def randomPlace(board,k):
    if move=='R':
        dict = {}
        j = 0
        count = 0
        for i in range(n):
            if board[i][j]==0:
                dict[count]=i
                count+=1
        return [dict[k%count],j]
    elif move=='L':
        dict = {}
        j = n-1
        count = 0
        for i in range(n):
            if board[i][j]==0:
                dict[count]=i
                count+=1
        return [dict[k%count],j]
    elif move=='U':
        dict = {}
        i = n-1
        count = 0
        for j in range(n):
            if board[i][j]==0:
                dict[count]=j
                count+=1
        return [i,dict[k%count]]
    elif move=='D':
        dict = {}
        i = 0
        m = 0
        for j in range(n):
            if board[i][j]==0:
                dict[m]=j
                m+=1
        return [i,dict[k%m]]


def move_test( board , x):
        test = []
        move =  x
        for i in range(n):
            help = []
            for j in range(n):
                help+=[board[i][j]]
            test += [help]
        if move =='R':
            if R_fun(board)==test :
                return True
        elif move =='L':
            if L_fun(board)==test:
                return True
        elif move =='U':
            if U_fun(board)==test:
                return True
        elif move =='D':
            if D_fun(board)==test:
                return True
        return  False


n = int(input())
board = []
for i in range(n):
    inp = input().split()
    for j in range(n):
        inp[j]=int(inp[j])
    board+=[inp]
numberOfMove = int(input())
dict = {
    0 : 'L',
    1 : 'D',
    2 : 'R',
    3 : 'U'
}

way = ""
movement = []
for i in range(numberOfMove):
    inp = input().split()
    for j in range(len(inp)):
        inp[j]=int(inp[j])
    movement+=[inp]


m = 0
count = 0
flaq = True
for i in range(numberOfMove):
    test = []
    for i in range(n):
        help = []
        for j in range(n):
            help+=[board[i][j]]
        test += [help]
    move = dict[m%4]
    if move =='R':
        R_fun(board)
        if board==test:
            flaq = False
        else:
            way+="R"
    elif move =='L':
        L_fun(board)
        if board==test:
            flaq = False
        else:
            way+="L"
    elif move =='U':
        U_fun(board)
        if board==test:
            flaq = False
        else:
            way+="U"
    elif move =='D':
        D_fun(board)
        if board==test:
            flaq = False
        else:
            way+="D"
    if flaq :
        k = movement[count][0]
        d = movement[count][1]
        count+=1
        list = randomPlace(board,k)
        board[list[0]][list[1]] = d
    test_board = []
    for i in range(n):
        help = []
        for j in range(n):
            help+=[board[i][j]]
        test_board += [help]
    if move_test(test_board,move):
        m+=1
    flaq = True
print(way)
for i in board:
    for j in i:
        print(j , end = '\t')
    print()



test = []
for i in range(n):
    help = []
    for j in range(n):
        help+=[board[i][j]]
    test += [help]
score = 0
for i in range(n):
    for j in range(n):
        if board[i][j]!=1 and board[i][j]!=2 and board[i][j]!=0:
            num = board[i][j]//3
            count = 0
            while num!=1:
                num = num//2
                count += 1
            score+=3**(count+1)
test1 = R_fun(board)
board = test
test2 = L_fun(board)
board = test
test3 = U_fun(board)
board = test
test4 = D_fun(board)
if test1==test and test2==test and test3==test and test4==test:
    print("The final score is " + str(score) + ".")
else:
    print("The partial score is " + str(score) + ".")
