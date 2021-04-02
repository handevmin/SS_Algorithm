import sys

N = int(sys.stdin.readline())

input_row = []
area = []
for i in range(N):
    input_row = list(map(int, sys.stdin.readline().split()))
    area.append(input_row)

election_area = [[0]*N for i in range(N)]
minimum = 40000

for x in range(1, N):
    for y in range(2, N):
        for d1 in range(1, N):
            for d2 in range(1, N):
                election_area = [[0] * N for i in range(N)]
                one, two, three, four, five = 0,0,0,0,0
                # 5번 구역
                if x > x+d1+d2 or x+d1+d2 > N or 1 > y-d1 or y-d1 >= y or y >= y+d2 or y+d2 > N:
                    continue
                for i in range(d1+1):
                    election_area[x+i-1][y-i-1] = 5
                    election_area[x+d2+i-1][y+d2-i-1] = 5
                for j in range(d2+1):
                    election_area[x+j-1][y+j-1] = 5
                    election_area[x+d1+j-1][y-d1+j-1] = 5
                
                # 1번 구역
                for r in range(x+d1-1):
                    for c in range(y):
                        if election_area[r][c] == 5:
                            break
                        election_area[r][c] = 1

                # 2번 구역
                for r in range(x+d2):
                    for c in reversed(range(y,N)):
                        if election_area[r][c] == 5:
                            break
                        election_area[r][c] = 2

                # 3번 구역
                for r in range(x+d1-1, N):
                    for c in range(y-d1+d2-1):
                        if election_area[r][c] == 5:
                            break
                        election_area[r][c] = 3

                # 4번 구역
                for r in range(x+d2, N):
                    for c in reversed(range(y-d1+d2-1, N)):
                        if election_area[r][c] == 5:
                            break
                        election_area[r][c] = 4

                for i in range(N):
                    for j in range(N):
                        if election_area[i][j] == 1:
                            one += area[i][j]
                        elif election_area[i][j] == 2:
                            two += area[i][j]
                        elif election_area[i][j] == 3:
                            three += area[i][j]
                        elif election_area[i][j] == 4:
                            four += area[i][j]
                        else :
                            five += area[i][j]

                merge = [one, two, three, four, five]
                gap = max(merge) - min(merge)
                if gap < minimum:
                    minimum = gap

print(minimum)
