import sys

N, M, K = map(int, sys.stdin.readline().split())
print(N)
board = []
for i in range(N):
    board.append(list(map(int, (sys.stdin.readline().split()))))
print(board)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
shark = {}
for i in range(M):
    for j in range(4):
        list(map(int, sys.stdin.readline().split()))