S = input()

for i in range(97, 123):
    ch = chr(i)

    if ch in S:
        print(S.find(ch), end=" ")
    else:
        print(-1, end=" ")
