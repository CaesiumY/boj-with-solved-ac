c_N, c_M = 8, 8
w_cnt, b_cnt = 0, 0
min_cnt = c_N * c_M

N, M = list(map(int, input().split()))
chess_table = []

for i in range(N):
    chess_table.append(input())

# w로 시작할 때와 b로 시작할 때 따로 또 세어줘야 함
for j in range(N - (c_N - 1)):
    for k in range(M - (c_M - 1)):
        w_cnt = 0
        b_cnt = 0

        for low in range(j, j + c_N):
            for col in range(k, k + c_M):
                if low % 2 == 0 and col % 2 == 0:
                    if chess_table[low][col] == "B":
                        w_cnt += 1
                elif low % 2 == 0 and col % 2 == 1:
                    if chess_table[low][col] == "W":
                        w_cnt += 1
                elif low % 2 == 1 and col % 2 == 1:
                    if chess_table[low][col] == "B":
                        w_cnt += 1
                elif low % 2 == 1 and col % 2 == 0:
                    if chess_table[low][col] == "W":
                        w_cnt += 1

        for low in range(j, j + c_N):
            for col in range(k, k + c_M):
                if low % 2 == 0 and col % 2 == 0:
                    if chess_table[low][col] == "W":
                        b_cnt += 1
                elif low % 2 == 0 and col % 2 == 1:
                    if chess_table[low][col] == "B":
                        b_cnt += 1
                elif low % 2 == 1 and col % 2 == 1:
                    if chess_table[low][col] == "W":
                        b_cnt += 1
                elif low % 2 == 1 and col % 2 == 0:
                    if chess_table[low][col] == "B":
                        b_cnt += 1

        min_cnt = min(min_cnt, w_cnt, b_cnt)


print(min_cnt)