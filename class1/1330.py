user_input = list(map(int, input().split()))


def sol(user_input):
    if user_input[0] < user_input[1]:
        return "<"

    if user_input[0] > user_input[1]:
        return ">"

    if user_input[0] == user_input[1]:
        return "=="


print(sol(user_input))