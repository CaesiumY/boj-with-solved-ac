length = int(input())
arr = list(map(int, input().split()))
max_number = max(arr)

for i in range(length):
    arr[i] = arr[i] / max_number * 100


print(sum(arr) / len(arr))