import sys

board = []
result = 0
resultlist = []
for i in range(4):
    data = sys.stdin.readline().split()
    row = []
    for j in range(0,8,2):
        row.append(list(map(int,data[j:j+2])))
    board.append(row)
print(board)

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

def move(board):
    for k in range(1, 17):
        # 이중 for문 빠져나가기 위한 세팅
        flag = False
        for i in range(4):
            for j in range(4):
                if board[i][j][0] == k:
                    flag = True
                    ################# 코드 리팩토링 ###################
                    dir_num = board[i][j][1]-1
                    # 움직이는 방향에 상어가 있거나 벽이면
                    while i+dr[dir_num]<0 or i+dr[dir_num]>3 or j+dc[dir_num]<0 or j+dc[dir_num]>3:
                        board[i][j][1] = (board[i][j][1]+1)% 8
                        dir_num = board[i][j][1] - 1
                    if board[i+dr[dir_num]][j+dc[dir_num]][0] == 0:
                        board[i][j][1] = (board[i][j][1] + 1) % 8
                        dir_num = board[i][j][1] - 1
                    while i+dr[dir_num]<0 or i+dr[dir_num]>3 or j+dc[dir_num]<0 or j+dc[dir_num]>3:
                        board[i][j][1] = (board[i][j][1]+1)% 8
                        dir_num = board[i][j][1] - 1
                    ##################################################
                    temp = board[i+dr[dir_num]][j+dc[dir_num]]
                    board[i + dr[dir_num]][j + dc[dir_num]] = board[i][j]
                    board[i][j] = temp
                    break
            if flag == True:
                break
def dfs(board, row, col, result):
    print("result", result)
    update_board = board[:]
    if row < 0 or row > 3 or col < 0 or col > 3:
        resultlist.append(result)
        return
    if update_board[row][col][0] == 0:
        resultlist.append(result)
        return

    shark_dir = update_board[row][col][1]-1
    fish_num = update_board[row][col][0]
    update_board[row][col][0] = 0
    move(update_board)
    print(update_board)
    for mul in range(1,4):
        dfs(board, row + dr[shark_dir]*mul, col + dc[shark_dir]*mul, result + fish_num)

dfs(board[:], 0, 0, 0)
print(resultlist)
print(board)