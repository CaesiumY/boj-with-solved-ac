result = []

while True:
    a, b = list(map(int, input().split()))
    if a == 0 and b == 0:
        break
    result.append(a + b)

for j in result:
    print(j)
