import os
import sys

X = {'x': 1, 'o': 2, '+': 1}

def debug(msg, arr):
    print "------"
    for i in arr:
        print "".join(i)
    print msg
    print "------"

def check(arr, N, x, y):
    num = 0
    hasPlus = False
    for i in range(N):
        c = arr[x][i]
        if c != ".":
            num += 1
            if c == "+":
                hasPlus = True

    if num > 1 and not hasPlus:
        #debug("p1", arr)
        return False

    num = 0
    hasPlus = False
    for i in range(N):
        c = arr[i][y]
        if c != ".":
            num += 1
            if c == "+":
                hasPlus = True

    if num > 1 and not hasPlus:
        #debug("p2", arr)
        return False

    num = 0
    hasX = False
    i = x
    j = y
    while x >= 0 and y >= 0:
        c = arr[x][y]
        if c != ".":
            num += 1
            if c == "x":
                hasX = True
        x -= 1
        y -= 1
        
    x = i + 1
    y = j + 1
    while x < N and y < N:
        c = arr[x][y]
        if c != ".":
            num += 1
            if c == "x":
                hasX = True
        x += 1
        y += 1
    if num > 1 and not hasX:
        #debug("p3", arr)
        return False
    
    num = 0
    hasX = False
    x = i
    y = j
    while x >= 0 and y < N:
        c = arr[x][y]
        if c != ".":
            num += 1
            if c == "x":
                hasX = True
        x -= 1
        y += 1
        
    x = i + 1
    y = j - 1
    while x < N and y >= 0:
        c = arr[x][y]
        if c != ".":
            num += 1
            if c == "x":
                hasX = True
        x += 1
        y -= 1
    if num > 1 and not hasX:
        #debug("p4", arr)
        return False

    debug("ok", arr)

    return True


def search(arr, x, y, N, result, final):
    print "x=%s, y=%s, result=%s" % (x, y, result)
    ret = 0
    if arr[x][y] == ".":
        if x < N - 1:
            print "search1 (%s, %s): %s" % (x, y, result)
            val = search(arr, x+1, y, N, result, final)
            if ret < val:
                ret = val
                del final[:]
                for i in result:
                    final.append(i)
        if y < N - 1:
            print "search2 (%s, %s): %s" % (x, y, result)
            val = search(arr, x, y+1, N, result, final)
            if ret < val:
                ret = val
                del final[:]
                for i in result:
                    final.append(i)
               
                #final = [i for i in result]
        for c, v in X.iteritems():
            arr[x][y] = c
            if check(arr, N, x, y):
                val = v
                result.append([c, x, y])
                if x < N - 1:
                    print "search3 (%s, %s): %s" % (x, y, result)
                    val = v + search(arr, x+1, y, N, result, final)
                if y < N - 1:
                    print "search4 (%s, %s): %s" % (x, y, result)
                    val = v + search(arr, x, y+1, N, result, final)
                if ret < val:
                    ret = val
                    del final[:]
                    for i in result:
                        final.append(i)

                    #final = [i for i in result]
                    print "max: %s, final: %s, result: %s" % (ret, final, result)
                del result[:-1]
            else:
                pass
            arr[x][y] = "."            
    else:
        backup = arr[x][y]
        if arr[x][y] != 'o':
            if x < N - 1:
                print "search5 (%s, %s): %s" % (x, y, result)
                val = X[backup] + search(arr, x+1, y, N, result, final)
            if y < N - 1:
                print "search6 (%s, %s): %s" % (x, y, result)
                val = X[backup] + search(arr, x, y+1, N, result, final)
            if ret < val:
                ret = val
                del final[:]
                for i in result:
                    final.append(i)
                
                #final = [i for i in result]

            arr[x][y] = 'o'
            if check(arr, N, x, y):
                result.append(['o', x, y])                
                val = 2
                if x < N - 1:
                    print "search7 (%s, %s): %s" % (x, y, result)
                    val = X['o'] + search(arr, x+1, y, N, result, final)
                if y < N - 1:
                    print "search8 (%s, %s): %s" % (x, y, result)
                    val = X['o'] + search(arr, x, y+1, N, result, final)
                if ret < val:
                    ret = val

                    del final[:]
                    for i in result:
                        final.append(i)
                    
                    #final = [i for i in result]
                    print "max: %s, final: %s" % (ret, final)
                        
                del result[:-1]
            else:
                pass
        arr[x][y] = backup

    print "ret: %s, %s" % (ret, result)

    return ret


if __name__ == "__main__":
    num = int(sys.stdin.readline().strip())
    for case in range(num):
        input = sys.stdin.readline().strip()
        N = int(input.split(" ")[0])
        M = int(input.split(" ")[1])
        arr = []
        for i in range(N):
            arr.append(["." for j in range(N)])
        for i in range(M):
            input = sys.stdin.readline().strip()
            tmp = input.split(" ")
            x = int(tmp[1]) - 1
            y = int(tmp[2]) - 1
            arr[x][y] = tmp[0]

        result = []
        final = []
        print search(arr, 0, 0, N, result, final)
        print final




