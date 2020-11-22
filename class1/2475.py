user_input = list(map(int, input().split()))

for i in range(len(user_input)):
    user_input[i] = user_input[i] ** 2


print(sum(user_input) % 10)