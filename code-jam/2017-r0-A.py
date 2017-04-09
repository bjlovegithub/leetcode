import os
import sys

def update(s, i):
    if s[i] == "+":
        s[i] = "-"
        return False
    elif s[i] == "-":
        s[i] = "+"
        return True

if __name__ == "__main__":
    num = int(sys.stdin.readline().strip())
    for case in range(num):
        input = sys.stdin.readline().strip()
        s = [i for i in input.split(" ")[0]]
        num = int(input.split(" ")[1])

        move = 0
        i = 0
        while i < len(s):
            if s[i] == "-":
                if i < len(s) - num + 1:
                    inc = 0
                    flag = True
                    for j in range(num):
                        ret = update(s, i+j)
                        if ret and flag:
                            inc += 1
                        else:
                            flag = False
                    move += 1
                    i += inc
                else:
                    move = -1
                    i += 1
            else:
                i += 1

        if move != -1:
            print "Case #%s: %s" % (case + 1, move)
        else:
            print "Case #%s: IMPOSSIBLE" % (case + 1)
