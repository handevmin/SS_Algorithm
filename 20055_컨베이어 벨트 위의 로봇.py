import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
belt = list(map(int, sys.stdin.readline().split()))
conveyor_belt = deque([])
robot_location = deque([])
robot = 1
robot_list = []
result = 0
count = 0

for i in belt:
    conveyor_belt.append(i)
    robot_location.append(0)

while count < K:
    # 자리이동
    conveyor_belt.rotate()
    robot_location.rotate()

    # 내려오는 자리일 때
    if robot_location[N-1] != 0:
        if result != 0:
            robot_list.remove(robot_location[N-1])
        robot_location[N-1] = 0

    # 로봇 이동
    for robot_num in robot_list:
        robot_index = robot_location.index(robot_num)
        if conveyor_belt[robot_index+1] != 0 and robot_location[robot_index+1] == 0:
            robot_location[robot_index] = 0
            robot_location[robot_index+1] = robot_num
            conveyor_belt[robot_index+1] -= 1
            if conveyor_belt[robot_index+1] == 0:
                count += 1

    if robot_location[0] == 0 and conveyor_belt[0] != 0:
        robot_location[0] = robot
        robot_list.append(robot)
        conveyor_belt[0] -= 1
        if conveyor_belt[0] == 0:
            count += 1
        robot += 1

    # 내려오는 자리일 때
    if robot_location[N-1] != 0:
        robot_list.remove(robot_location[N-1])
        robot_location[N-1] = 0

    result += 1

print(result)