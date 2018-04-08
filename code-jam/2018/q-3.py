import sys

def solve(a):
    arr = []
    for i in range(30):
        iarr = [0 for i in range(30)]
        arr.append(iarr)

    if a == 20:
        bx = 4
        by = 5
    else:
        bx = 10
        by = 20

    while True:
        nx = 0
        ny = 0
        find = False
        for i in range(bx):
            if find:
                break
            for j in range(by):
                if arr[i+1][j+1] == 0:
                    nx = i + 1
                    ny = j + 1
                    find = True
                    break
        if nx == 1:
            nx = 2
        elif nx == bx:
            nx = bx - 1
        if ny == 1:
            ny = 2
        elif ny == by:
            ny = by - 1

        print("%d %d" % (nx, ny))
        sys.stdout.flush()
        
        x, y = [int(s) for s in raw_input().split(" ")]

        if (x == -1 and y == -1) or (x == 0 and y == 0):
            break

        arr[x][y] = 1

if __name__ == "__main__":
    t = int(raw_input())
    for i in xrange(1, t + 1):
        a = int(raw_input())
        solve(a)
        

