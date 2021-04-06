"""
입력
원판의 크기 N, 원판에 적힌 수의 갯수 M, 회전 수 T
원판에 적힌수
xi, di, ki : xi의 배수인 원판을 di 방향으로 ki칸 회전시킨다
"""

import sys
from collections import deque
from copy import deepcopy

N,M,T = map(int, sys.stdin.readline().split())

circle_board = []
circle_board.append(deque([0]*M))

for i in range(N):
    circle = deque(list(map(int, sys.stdin.readline().split())))
    circle_board.append(circle)

result = 0

for t in range(T):
    x, d, k = map(int, sys.stdin.readline().split())

    d = 1 if d == 0 else -1
    flag = False
    circle_sum = 0
    count = 0

    for i in range(1, N+1):
        if i % x == 0:
            circle_board[i].rotate(k*d)

    circle_board_copy = deepcopy(circle_board)

    for i in range(1, N + 1):
        for j in range(M):
            if circle_board[i][j] != 0:
                # 인접하면서 수가 같은 것이 없을 경우를 대비
                circle_sum += circle_board[i][j]
                count += 1

                # 인접하면서 수가 같은 것이 있으면
                if circle_board[i][j] == circle_board[i][j-1]:
                    circle_board_copy[i][j] = 0
                    circle_board_copy[i][j-1] = 0
                    flag = True
                if circle_board[i-1][j] == circle_board[i][j]:
                    circle_board_copy[i][j] = 0
                    circle_board_copy[i-1][j] = 0
                    flag = True
    if flag == False:
        for i in range(1, N + 1):
            for j in range(M):
                if circle_board_copy[i][j] != 0:
                    if circle_board_copy[i][j] > circle_sum/count:
                        circle_board_copy[i][j] -= 1
                    elif circle_board_copy[i][j] < circle_sum/count:
                        circle_board_copy[i][j] += 1
    circle_board = deepcopy(circle_board_copy)

for i in circle_board:
    result += sum(i)
print(result)