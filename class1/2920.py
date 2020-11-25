user_input = list(map(int, input().split()))

if user_input == sorted(user_input):
    print("ascending")
elif user_input == sorted(user_input, reverse=True):
    print("descending")
else:
    print("mixed")
