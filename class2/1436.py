c_num = "666"
user_input = int(input())
result = []
cnt = int(c_num)

while len(result) != user_input:

    if c_num in str(cnt):
        result.append(cnt)

    cnt += 1

print(result[-1])