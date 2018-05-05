def solve(arr):
    dp = [[] for i in arr]
    dp[0] = [arr[0], 1]
    for i in range(1, len(arr)):
        tolerate = arr[i] * 6
        maxLength = -1
        minWeight = -1
        all = 0
        for j in range(i):
            all += arr[j]
            if tolerate >= dp[j][0]:
                if maxLength == -1:
                    maxLength = dp[j][1] + 1
                    minWeight = dp[j][0] + arr[i]
                else:
                    if maxLength < dp[j][1] + 1:
                        maxLength = dp[j][1] + 1
                        minWeight = dp[j][0] + arr[i]
                    elif maxLength == dp[j][1] + 1:
                        if minWeight > dp[j][0] + arr[i]:
                            minWeight = dp[j][0] + arr[i]
        if maxLength == -1:
            dp[i] = [arr[i], 1]
        else:
            dp[i] = [minWeight, maxLength]

        
    maxLength = 1
    for i in dp:
        if maxLength < i[1]:
            maxLength = i[1]
    return maxLength
    
def stdin_input():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        N = int(raw_input())
        arr = [int(s) for s in raw_input().split(" ")]
            
        print "Case #%s: %s" % (i, solve(arr))

if __name__ == "__main__":
    stdin_input()
