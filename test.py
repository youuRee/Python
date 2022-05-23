# 1074
import sys
import math
N, r, c = map(int, sys.stdin.readline().split())
arr = []
lenth = int(math.pow(2, N))
visited = 0
def dac(x, y, n):
    global visited
    if n != 2:
        for i in range(x, x+n):
            for j in range(y, y+n):
                dac(x, y, n//2)
                dac(x, y+n//2, n//2)
                dac(x+n//2, y, n//2)
                dac(x+n//2, y+n//2, n//2)
                return
    else:
        arr[x][y] = visited
        visited += 1

dac(0, 0, lenth)