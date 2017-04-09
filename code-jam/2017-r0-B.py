import os
import sys

if __name__ == "__main__":
    num = int(sys.stdin.readline().strip())
    #fh = open("B-large.in")
    #num = int(fh.readline().strip())
    for case in range(num):
        input = sys.stdin.readline().strip()
        #input = fh.readline().strip()
        arr = [ord(c) - ord('0') for c in input]
        while True:
            hasChange = False
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    arr[i] -= 1
                    for j in range(i+1, len(arr)):
                        arr[j] = 9
                    hasChange = True
                    break

            if not hasChange:
                break

        s = "".join([str(i) for i in arr])
        s = s.lstrip("0")
        print "Case #%s: %s" % (case + 1, s)
    

