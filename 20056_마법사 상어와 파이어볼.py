import sys

N, M, K = map(int, sys.stdin.readline().split())

fireball = []
board = [[0] * (N) for i in range(N)]
m_board = [[[] for j in range(N)] for i in range(N)]
s_board = [[[] for j in range(N)] for i in range(N)]
d_board = [[[] for j in range(N)] for i in range(N)]

new_m_board = [[[] for j in range(N)] for i in range(N)]
new_s_board = [[[] for j in range(N)] for i in range(N)]
new_d_board = [[[] for j in range(N)] for i in range(N)]

for i in range(M):
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    fireball.append([r-1, c-1, m, s, d])
    m_board[r - 1][c - 1].append(m)
    s_board[r - 1][c - 1].append(s)
    d_board[r - 1][c - 1].append(d)

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
for i in range(K):
    new_m_board = [[[] for j in range(N)] for i in range(N)]
    new_s_board = [[[] for j in range(N)] for i in range(N)]
    new_d_board = [[[] for j in range(N)] for i in range(N)]
    for i in range(len(board)):
        for j in range(len(board[i])):
            for k in range(len(m_board[i][j])):
                # 이동하기 전
                row = i
                column = j

                # 이동한 후
                new_row = (row + dr[d_board[i][j][k]] * s_board[i][j][k]) % N
                new_column = (column + dc[d_board[i][j][k]] * s_board[i][j][k]) % N
                new_m_board[new_row][new_column].append(m_board[i][j][k])
                new_s_board[new_row][new_column].append(s_board[i][j][k])
                new_d_board[new_row][new_column].append(d_board[i][j][k])

    m_board = new_m_board
    s_board = new_s_board
    d_board = new_d_board
    for i in range(len(board)):
        for j in range(len(board[i])):
            if len(new_m_board[i][j]) >= 2:
                new_m = sum(m_board[i][j]) // 5
                if new_m != 0:
                    new_m_board[i][j] = [new_m for i in range(4)]
                    new_s = (sum(s_board[i][j]) // len(s_board[i][j]))
                    new_s_board[i][j] = [new_s for i in range(4)]
                    check = list(map(lambda x: x % 2, d_board[i][j]))

                    d_board_length = len(d_board[i][j])
                    new_m_board[i][j] = []
                    new_s_board[i][j] = []
                    new_d_board[i][j] = []

                    new_m_board[i][j] = [new_m, new_m, new_m, new_m]
                    new_s_board[i][j] = [new_s, new_s, new_s, new_s]
                    if sum(check) == 0 or sum(check) == d_board_length:
                        new_d_board[i][j] = [0, 2, 4, 6]
                    else:
                        new_d_board[i][j] = [1, 3, 5, 7]
                else:
                    new_m_board[i][j] = []
                    new_s_board[i][j] = []
                    new_d_board[i][j] = []

    m_board = new_m_board
    s_board = new_s_board
    d_board = new_d_board

result =0
for i in range(len(m_board)):
    for j in range(len(m_board[i])):
        result += sum(m_board[i][j])
print(result)