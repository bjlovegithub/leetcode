
def solve(cn, arr):
    odd_arr = []
    even_arr = []

    for i in range(len(arr)):
        if i % 2 == 0:
            even_arr.append(arr[i])
        else:
            odd_arr.append(arr[i])

    odd_arr.sort()
    even_arr.sort()

    pos = -1
    for i in range(min(len(odd_arr), len(even_arr))):
        if odd_arr[i] < even_arr[i]:
            pos = i * 2
            break
        if i+1 < len(even_arr) and odd_arr[i] > even_arr[i+1]:
            pos = i * 2 + 1
            break

    if pos == -1:
        print "Case #{}: OK".format(cn)
    else:
        print "Case #{}: {}".format(cn, pos)

if __name__ == "__main__":
    t = int(raw_input())
    for i in xrange(1, t + 1):
        n = int(raw_input())
        arr = [int(s) for s in raw_input().split(" ")]
        solve(i, arr)
        

