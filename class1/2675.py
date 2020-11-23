user_input = int(input())
codes = []
result = []

for i in range(user_input):
    codes.append(input().split())

for j in codes:
    code = ""
    for k in j[1]:
        code += k * int(j[0])
    result.append(code)

for l in result:
    print(l)
