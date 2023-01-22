def copy(board):
    test = []
    for i in range(n):
        help = []
        for j in range(n):
            help+=[board[i][j]]
        test += [help]
    return test
#this fuction makes a copy of my board.
def max(x):
    maximum = x[0]
    for i in x:
        if i>maximum:
            maximum=i
    return maximum
#this function gives the maximum of a list.
#--------------------------------------------------------------------------------------------------------------
def R_fun(board):
    maxMerge = 0
    merges = 0
    for j in range(n-1,0,-1):
        for i in range(n):
            if board[i][j]==0:
                board[i][j],board[i][j-1]=(board[i][j-1],board[i][j])
            else:
                merges = 0
                if board[i][j]==1 and board[i][j-1]==2:
                    board[i][j]=3
                    board[i][j-1]=0
                    merges = 3
                elif board[i][j]==2 and board[i][j-1]==1:
                    board[i][j]=3
                    board[i][j-1]=0
                    merges = 3
                elif board[i][j]!=1 and board[i][j]!=2 and board[i][j]==board[i][j-1]:
                    board[i][j]=2*(board[i][j])
                    board[i][j-1]=0
                    merges = (board[i][j])
                if merges>maxMerge:
                    maxMerge = merges
    return board,('R',maxMerge)

def L_fun(board):
    maxMerge = 0
    for j in range(0,n-1,):
        for i in range(n):
            if board[i][j]==0:
                board[i][j],board[i][j+1]=(board[i][j+1],board[i][j])
            else:
                merges = 0
                if board[i][j]==1 and board[i][j+1]==2:
                    board[i][j]=3
                    board[i][j+1]=0
                    merges = 3
                elif board[i][j]==2 and board[i][j+1]==1:
                    board[i][j]=3
                    board[i][j+1]=0
                    merges = 3
                elif board[i][j]!=1 and board[i][j]!=2 and board[i][j]==board[i][j+1]:
                    board[i][j]=2*(board[i][j])
                    board[i][j+1]=0
                    merges = (board[i][j])
                if merges>maxMerge:
                    maxMerge = merges
    return board,('L',maxMerge)

def U_fun(board):
    maxMerge = 0
    for i in range(0,n-1):
        for j in range(n):
            if board[i][j]==0:
                board[i][j],board[i+1][j]=(board[i+1][j],board[i][j])
            else:
                merges = 0
                if board[i][j]==1 and board[i+1][j]==2:
                    board[i][j]=3
                    board[i+1][j]=0
                    merges = 3
                elif board[i][j]==2 and board[i+1][j]:
                    board[i][j]=3
                    board[i+1][j]=0
                    merges = 3
                elif board[i][j]!=1 and board[i][j]!=2 and board[i][j]==board[i+1][j]:
                    board[i][j]=2*(board[i][j])
                    board[i+1][j]=0
                    merges = (board[i][j])
                if merges>maxMerge:
                    maxMerge = merges
    return board,('U',maxMerge)

def D_fun(board):
    maxMerge = 0
    for i in range(n-1,0,-1):
        for j in range(n):
            if board[i][j]==0:
                board[i][j],board[i-1][j]=(board[i-1][j],board[i][j])
            else:
                merges = 0
                if board[i][j]==1 and board[i-1][j]==2:
                    board[i][j]=3
                    board[i-1][j]=0
                    merges = 3
                elif board[i][j]==2 and board[i-1][j]:
                    board[i][j]=3
                    board[i-1][j]=0
                    merges = 3
                elif board[i][j]!=1 and board[i][j]!=2 and board[i][j]==board[i-1][j]:
                    board[i][j]=2*(board[i][j])
                    board[i-1][j]=0
                    merges = (board[i][j])
                if merges>maxMerge:
                    maxMerge = merges
    return board , ('D',maxMerge)
#these fuction are moving the element of the table like we want & count the maximum of the merge on that special move.
def randomPlace(board,k):
    if q=='R':
        dict = {}
        j = 0
        count = 0
        for i in range(n):
            if board[i][j]==0:
                dict[count]=i
                count+=1
        return [dict[k%count],j]
    elif q=='L':
        dict = {}
        j = n-1
        count = 0
        for i in range(n):
            if board[i][j]==0:
                dict[count]=i
                count+=1
        return [dict[k%count],j]
    elif q=='U':
        dict = {}
        i = n-1
        count = 0
        for j in range(n):
            if board[i][j]==0:
                dict[count]=j
                count+=1
        return [i,dict[k%count]]
    elif q=='D':
        dict = {}
        i = 0
        m = 0
        for j in range(n):
            if board[i][j]==0:
                dict[m]=j
                m+=1
        return [i,dict[k%m]]

#this function is making a random number for the empty places.
#--------------------------------------------------------------------------------------------------------------

def Convert(list):
    dictionry = {list[i]: list[i + 1] for i in range(0, len(list), 2)}
    return dictionry
#this function is coverting a list to a dictionry
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
n = int(input())
board = []
for i in range(n):
    inp = input().split()
    for j in range(n):
        inp[j]=int(inp[j])
    board+=[inp]
numberOfMove = int(input())
#getting the Matrix inputs.

way = ""
movement = []
for i in range(numberOfMove):
    inp = input().split()
    for j in range(len(inp)):
        inp[j]=int(inp[j])
    movement+=[inp]
#getting the random valuse as a list.
count = -1
for i in range(numberOfMove):
    dict = {}
    dict.update(Convert(L_fun(copy(board))[1]))
    dict.update(Convert(D_fun(copy(board))[1]))
    dict.update(Convert(R_fun(copy(board))[1]))
    dict.update(Convert(U_fun(copy(board))[1]))
    listHelp = list(dict.values())
    maximum = max(listHelp)
    for i in dict.keys():
        if dict[i]==maximum:
            if i=='L':
                L_fun(board)
                way+="L"
                count+=1
                q = "L"
                break
            elif i =='D':
                D_fun(board)
                way+="D"
                count+=1
                q = "D"
                break
            elif i =='R':
                R_fun(board)
                way+="R"
                count+=1
                q = "R"
                break
            elif i =='U':
                U_fun(board)
                way+="U"
                count+=1
                q = "U"
                break
    k = movement[count][0]
    d = movement[count][1]
    lst = randomPlace(board,k)
    board[lst[0]][lst[1]]=d
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
print(way)
for i in board:
    for j in i:
        print(j , end = '\t')
    print()
#printing the final board and moves.



#the main caculating of this phase.
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
#calculating the score and copy the matrix to compare .