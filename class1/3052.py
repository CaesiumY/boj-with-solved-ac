user_input = []

for i in range(10):
    user_input.append(int(input()) % 42)

print(len(set(user_input)))