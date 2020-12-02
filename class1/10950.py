user_input = int(input())
result = []

for i in range(user_input):
    a, b = list(map(int, input().split()))
    result.append(a + b)

for j in result:
    print(j)
