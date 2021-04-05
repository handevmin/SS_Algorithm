"""
- Input
체스판의 크기 N, 말의 개수 K
체스판의 정보 (0은 흰색, 1은 빨간색, 2는 파란색)
말의 정보 (행, 열, 말의 방향)

1. 1번말부터 반복문을 돌리며 방향대로 이동한다.
2. 이동한 칸에 따른 조건을 수행한다
   if
"""

import sys
#sys.stdin = open("input.txt", "r")

N, K = map(int,sys.stdin.readline().split())
board = []
turn = 0
flag = False

for i in range(N):
    board_row = list(map(int, sys.stdin.readline().split()))
    board.append([])

    for j in board_row:
        if j == 1:
            board[i].append({'R':''})
        elif j == 2:
            board[i].append({'B':''})
        else:
            board[i].append({'W':''})

piece = {}
for i in range(K):
    if i == 9:
        piece[0] = list(map(int, sys.stdin.readline().split()))
        break
    piece[i+1] = list(map(int, sys.stdin.readline().split()))

# 체스판 위에 말을 놓고 시작한다
for i in piece:
    if i == 10:
        board[piece[i][0] - 1][piece[i][1] - 1][list(board[piece[i][0] - 1][piece[i][1] - 1].keys())[0]] += str(0)
        break
    board[piece[i][0]-1][piece[i][1]-1][list(board[piece[i][0]-1][piece[i][1]-1].keys())[0]] += str(i)

dr = [0,0,-1,1]
dc = [1,-1,0,0]

def turn_opposite(i):
    global move_piece
    global nr
    global nc

    # 반대방향으로 전환
    if piece[i][2]%2==0:
       piece[i][2] -= 1
    else:
        piece[i][2] += 1

    nr = piece[i][0]-1 + dr[piece[i][2]-1]
    nc = piece[i][1]-1 + dc[piece[i][2]-1]

    # 범위를 벗어낫거나 이동하려는 칸이 파란색인 경우
    if nr < 0 or nr >= N or nc < 0 or nc >= N or list(board[nr][nc].keys())[0] == 'B':
        return 1
    # 반대방향으로 이동한 칸이 빨간색일 경우
    elif list(board[nr][nc].keys())[0] == 'R':
        board[nr][nc]['R'] += move_piece[::-1]
    else:
        board[nr][nc]['W'] += move_piece

while turn < 1001:
    for i in piece:
        nr = piece[i][0]-1 + dr[piece[i][2]-1]
        nc = piece[i][1]-1 + dc[piece[i][2]-1]

        # 현재 위치의 색
        current_color = list(board[piece[i][0]-1][piece[i][1]-1].keys())[0]
        # 현재 위치의 놓여있는 말
        current_state = board[piece[i][0]-1][piece[i][1]-1][current_color]

        move_piece = current_state[current_state.index(str(i)):]        # 움직일 말
        remain_piece = current_state[:current_state.index(str(i))]           # 남겨진 말

        if 0<=nr<N and 0<=nc<N:
            next_color = list(board[nr][nc].keys())[0]

            # 흰색인 경우
            if next_color == 'W':
                board[nr][nc]['W'] += str(move_piece)

            # 빨간색인 경우
            elif next_color == 'R':
                board[nr][nc]['R'] += move_piece[::-1]
            # 파란색인 경우
            else:
                if turn_opposite(i) == True: continue
        else:
            if turn_opposite(i) == True: continue

        board[piece[i][0] - 1][piece[i][1] - 1][current_color] = remain_piece  # 현재 위치에 있는 말 갱신

        for j in move_piece:
            piece[int(j)][0], piece[int(j)][1] = nr+1, nc+1  # 말의 위치 갱신

        # 현재 색과 상태 업데이트
        current_color = list(board[piece[i][0] - 1][piece[i][1] - 1].keys())[0]
        current_state = board[piece[i][0]-1][piece[i][1]-1][current_color]

        if len(current_state) >= 4:
            flag = True
            break

    turn += 1

    if flag ==True:
        break

if turn > 1000:
    turn = -1

print(turn)


