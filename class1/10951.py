import sys

for i in sys.stdin:  # EOF 까지 입력을 받는다.
    a, b = list(map(int, i.split()))
    print(a + b)
