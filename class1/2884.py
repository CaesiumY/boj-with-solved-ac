user_input = list(map(int, input().split()))

user_input[1] -= 45

if user_input[1] < 0:
    user_input[0] -= 1
    user_input[1] += 60

if user_input[0] < 0:
    user_input[0] += 24

print(user_input[0], user_input[1])
