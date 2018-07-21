def search(currentIndex, endIndex, arr, words, word):
    for c in arr[currentIndex]:
        newWord = word + c
        if currentIndex == endIndex:
            if newWord not in words:
                return newWord
        else:
            result = search(currentIndex+1, endIndex, arr, words, newWord)
            if result != None:
                return result

    return None

def solve(arr, words):
    result = search(0, len(arr)-1, arr, words, '')
    if result is None:
        return "-"
    else:
        return result
    
def stdin_input():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        N, L = [int(s) for s in raw_input().split(" ")]
        arr = []
        for j in range(L):
            arr.append({})
        words = {}
        for j in range(N):
            s = raw_input()
            idx = 0
            for c in s:
                arr[idx][c] = 1
                idx += 1
            words[s] = 1
            
        print "Case #%s: %s" % (i, solve(arr, words))

if __name__ == "__main__":
    stdin_input()
