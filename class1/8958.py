user_input = int(input())
oxs = []
results = []

for i in range(user_input):
    oxs.append(input())

for j in range(len(oxs)):
    flag = 0
    score = 0
    for k in range(len(oxs[j])):
        if oxs[j][k] == "O":
            flag += 1
        else:
            flag = 0

        score += flag
    results.append(score)


for l in results:
    print(l)
