import sys

N, M, K = map(int, sys.stdin.readline().split())

fireball = []
board = [[0]*(N) for i in range(N)]
m_s_board = [[] for j in range(N)] for i in range(N)
for i in range(M):
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    fireball.append([r,c,m,s,d])
    board[r-1][c-1] = 1
print(m_s_board)
print(board)

dr = [1, 1, 0, -1, -1, -1, 0, 1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

board[fireball[i][0]-1][fireball[i][1]-1]/
for i in range(K+1):
    row = fireball[i][0]
    column = fireball[i][1]
    board[row-1][column-1]-=1
    row += dr[fireball[i][4]]*fireball[i][3]
    column += dc[fireball[i][4]]*fireball[i][3]
    row %= N
    column %= N
    board[row-1][column-1] = fireball[i]



print(board)