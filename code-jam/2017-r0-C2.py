import os
import sys

if __name__ == "__main__":
    num = int(sys.stdin.readline().strip())
    for case in range(num):
        input = sys.stdin.readline().strip()
        N = int(input.split(" ")[0])
        K = int(input.split(" ")[1])

        arr = {N: 1}
        maxN = -1        

        while K > 0:
            maxN = -1
            for i in arr:
                if maxN < i:
                    maxN = i

            #print maxN, K, arr

            if maxN <= 1 or K == 1:
                break

            K -= arr[maxN]

            if K > 0:
                l = maxN / 2
                if l in arr:
                    arr[l] += arr[maxN]
                else:
                    arr[l] = arr[maxN]

                r = maxN - 1 - maxN / 2
                if r > 0:
                    if r in arr:
                        arr[r] += arr[maxN]
                    else:
                        arr[r] = arr[maxN]

                del arr[maxN]

        l = maxN / 2
        r = maxN - 1 - maxN / 2
        if r < 0:
            r = 0
        print "Case #%s: %s %s" % (case + 1, l, r)
            
            
            
