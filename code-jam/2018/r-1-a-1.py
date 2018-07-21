def get_total(arr):
    total = 0
    for s in arr:
        for c in s:
            if c == '@':
                total += 1

    return total

def check(h, v, arr):
    lj = len(arr[0])
    c0 = c1 = c2 = c3 = 0
    for i in range(len(arr)):
        for j in range(lj):
            if arr[i][j] == '@':
                if i <= h:
                    if j <= v:
                        c0 += 1
                    else:
                        c2 += 1
                else:
                    if j <= v:
                        c1 += 1
                    else:
                        c3 += 1
    return c1 == c2 and c1 == c3 and c1 == c0

def solve(R, C, H, V, arr):
    total = get_total(arr)

    if total % ((H+1)*(V+1)) != 0:
        return "IMPOSSIBLE"

    for h in range(R-1):
        for v in range(C-1):
            if check(h, v, arr):
                return "POSSIBLE"

    return "IMPOSSIBLE"
    
def stdin_input():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        R, C, H, V = [int(s) for s in raw_input().split(" ")]
        arr = []
        for j in range(R):
            arr.append(raw_input())
            
        print "Case #%s: %s" % (i, solve(R, C, H, V, arr))
    

if __name__ == "__main__":
    stdin_input()
