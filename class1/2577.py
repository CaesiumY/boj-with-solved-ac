times_number = 1
result = [0 for i in range(10)]

for i in range(3):
    times_number *= int(input())

for j in str(times_number):
    result[int(j)] += 1

for k in result:
    print(k)
