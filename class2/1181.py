user_input = int(input())
user_list = []
result = []

for i in range(user_input):
    user_list.append(input())

for j in sorted(user_list, key=lambda x: (len(x), x)):
    if j not in result:
        result.append(j)

for k in result:
    print(k)
