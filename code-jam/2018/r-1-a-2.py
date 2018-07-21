def make_order(arr):
    for i in arr:
        i.append((i[0]*i[1]+i[2])/i[0])

    arr.sort(key = lambda x: x[3])

    return arr

def solve(R, B, C, arr):
    arr = make_order(arr)
    print arr

    curr = 0
    in_use = {}
    in_use_num = 0
    for i in range(len(arr)):
        in_use[i] = 0

    while B > 0:
        curr = in_use[0]
        for k in in_use:
            if curr == 0:
                curr = in_use[k]
            elif in_use[k] != 0 and curr > in_use[k]:
                curr = in_use[k]

        in_use_num = 0
        for k in in_use:
            if in_use[k] > curr:
                in_use_num += 1

        print curr, in_use                                

        avg = B / (R - in_use_num)
        if avg == 0:
            avg = 1

        for i in range(len(arr)):
            if B <=0:
                break
            if in_use[i] == curr:
                if in_use_num < R:
                    b_num = min(avg, arr[i][0])
                    in_use[i] = curr + (b_num*arr[i][1]+arr[i][2])
                    in_use_num += 1
                    B -= b_num
                else:
                    pass
        print in_use, B

    print in_use
    ret = in_use[0]
    for k in in_use:
        if ret < in_use[k]:
            ret = in_use[k]

    return ret
    
def stdin_input():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        R, B, C = [int(s) for s in raw_input().split(" ")]
        arr = []
        for j in range(C):
            arr.append([int(s) for s in raw_input().split(" ")])
            
        print "Case #%s: %s" % (i, solve(R, B, C, arr))
    

if __name__ == "__main__":
    stdin_input()
