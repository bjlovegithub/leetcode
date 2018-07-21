import os
import sys

if __name__ == "__main__":
    num = int(sys.stdin.readline().strip())
    for case in range(num):
        input = sys.stdin.readline().strip()
        R = int(input.split(" ")[0])
        C = int(input.split(" ")[1])

        cake = []
        startEnd = []
        for row in range(R):
            input = sys.stdin.readline().strip()
            arr = []
            col = 0
            for c in input:
                arr.append(c)
                if c != "?":
                    startEnd.append = [row, col, c]
                col += 1
            cake.append(arr)

        print cake
        print startEnd

        for i in len(startEnd):
            startEnd[i].append([0, 0, row, col])

            if i == len(startEnd) - 1:
                if i != 0:
                    prev = startEnd[i-1][3]
                    curr = startEnd[i][3]

                    if prev[3] == curr[0]:
                        curr[3] = prev[3]
                        curr[4] = prev[4] + 1
                    else:
                        curr[3] = prev[3] + 1
                    
                
        
