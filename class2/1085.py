x, y, w, h = list(map(int, input().split()))

to_top = h - y
to_bottom = y
to_right = w - x
to_left = x

print(min(to_top, to_bottom, to_right, to_left))