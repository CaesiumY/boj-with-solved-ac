K, N = list(map(int, input().split()))
arr = []

for i in range(K):
    arr.append(int(input()))

start, end = 1, max(arr)

while start <= end:
    goal = 0
    mid = (start + end) // 2

    for j in arr:
        goal += j // mid

    if goal >= N:
        start = mid + 1
    else:
        end = mid - 1


print(end)
