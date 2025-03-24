import sys
n=int(input(" enter the number for length of star:"))
screen_width = 70
for i in range(1, n + 1):
    stars = "*" * (2* i - 1)
    print(stars.center(screen_width) + "\n")
for i in range(n - 1, 0, -1):
    stars = "*" * (2 * i - 1)
    print(stars.center(screen_width) + "\n")
