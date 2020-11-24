user_input = input().split()
result = []

for i in user_input:
    result.append(int("".join(reversed(i))))

print(max(result))