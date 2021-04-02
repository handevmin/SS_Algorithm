"""
연구소의 크기 N(4 ≤ N ≤ 50) 바이러스의 개수 M(1 ≤ M ≤ 10)
0은 빈 칸, 1은 벽, 2는 바이러스
전체 바이러스의 개수 중의 M개 만큼 바이러스를 활성화
1. 입력받을 때 시간만 숫자로 표현 (입력받을 때 초기화하는 방안 고민)
2. 입력받을 때 바이러스의 위치를 저장하고 그 중 M개만 뽑는 combination
3. 각 combination 요소를 돌면서 시간이 증가할 때마 바이러스 상, 하, 좌, 우 값 +1 하고 all 함수로 체크
4. max 값을 저장하고 3번을 돌 때 max보다 크면 break 작으면 max 값 업데이트
5. 모든 combination 요소에 대해서 반복횟수가 2000번 이상이면 -1 출력
"""

import sys
from itertools import combinations
from collections import deque

N, M = map(int, sys.stdin.readline().split())
lab = []
virus = []
time_list = []

# 입력과 동시에 시간만 숫자로 표현
for i in range(N):
    input_row = list(map(int, sys.stdin.readline().split()))
    lab.append([])
    for index, value in enumerate(input_row):
        if value == 1:
            lab[i].append('-')
        elif value == 2:
            lab[i].append('*')
            virus.append([i, index])
        else:
            lab[i].append(0)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 바이러스가 퍼지는 함수 (dfs)
def extend(selected_virus):
    max = 2000     # 최악의 조건일때 걸리는 시간

    queue = deque([])
    check = 0  # 모든 빈 칸에 바이러스가 퍼졌는지 확인

    for i in selected_virus:
        # 큐에 바이러스의 위치와 시간을 넣어준다
        queue.append(i + [0])
        visited[i[0]][i[1]] = True

    while queue:
        virus = queue.popleft()
        time = virus[2]           # virus = [r,c,time]
        # 상, 하 좌, 우의 값 +1
        for i in range(4):
            if 0 <= virus[0]+dr[i] < N and 0 <= virus[1] + dc[i] < N:

                # 새로 전파할 위치
                new_location = new_lab[virus[0] + dr[i]][virus[1] + dc[i]]

                # 새로운 위치가 벽도 바이러스도 아니고 방문하지도 않았을 때
                if new_location != '-' and new_location != '*' and not visited[virus[0]+dr[i]][virus[1] + dc[i]]:
                    new_lab[virus[0]+dr[i]][virus[1] + dc[i]] = time+1      # 시간 증가
                    queue.append([virus[0]+dr[i], virus[1] + dc[i], time+1])     # 큐에 삽입
                    visited[virus[0]+dr[i]][virus[1] + dc[i]] = True     # 방문 처리

    # 실험식에 벽에 막혀 전파되지 않은 공간이 있는지 체크
    for i in new_lab:
        if all(i):
            check+=1

    if check == N:
        return time
    else:
        return max

def extend_ignore_virus(selected_virus):
    max = 2000     # 최악의 조건일때 걸리는 시간

    queue = deque([])
    check = 0  # 모든 빈 칸에 바이러스가 퍼졌는지 확인

    for i in selected_virus:
        # 큐에 바이러스의 위치와 시간을 넣어준다
        queue.append(i + [0])
        visited_ignore_virus[i[0]][i[1]] = True

    while queue:
        virus = queue.popleft()
        time = virus[2]           # virus = [r,c,time]
        # 상, 하 좌, 우의 값 +1
        for i in range(4):
            if 0 <= virus[0]+dr[i] < N and 0 <= virus[1] + dc[i] < N:

                # 새로 전파할 위치
                new_location = new_lab_ignore_virus[virus[0] + dr[i]][virus[1] + dc[i]]

                # 새로운 위치가 벽도 바이러스도 아니고 방문하지도 않았을 때
                if new_location != '-' and not visited_ignore_virus[virus[0]+dr[i]][virus[1] + dc[i]]:
                    new_lab_ignore_virus[virus[0]+dr[i]][virus[1] + dc[i]] = time+1      # 시간 증가
                    queue.append([virus[0]+dr[i], virus[1] + dc[i], time+1])     # 큐에 삽입
                    visited_ignore_virus[virus[0]+dr[i]][virus[1] + dc[i]] = True     # 방문 처리

    # 실험식에 벽에 막혀 전파되지 않은 공간이 있는지 체크
    for i in new_lab_ignore_virus:
        if all(i):
            check+=1

    if check == N:
        return time
    else:
        return max


# 각 combination 요소를 돌면서 바이러스를 퍼지게 한다
for selected_virus in list(combinations(virus, M)):

    new_lab = [item[:] for item in lab]
    visited = [[False]*N for i in range(N)]
    time_list.append(extend(selected_virus))

result = min(time_list)
if result != 2000:
    print(result)
else:
    for selected_virus in list(combinations(virus, M)):
        new_lab_ignore_virus = [item[:] for item in lab]
        visited_ignore_virus = [[False] * N for i in range(N)]
        time_list.append(extend_ignore_virus(selected_virus))
    result = min(time_list)
    if result == 2000:
        print(-1)
    else:
        print(result)
