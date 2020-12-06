user_list = []

while True:
    user_input = input()
    reversed_input = user_input[::-1]

    if user_input == "0":
        break

    if user_input == reversed_input:
        user_list.append("yes")
    else:
        user_list.append("no")

for i in user_list:
    print(i)
