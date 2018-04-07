
def solve(cn, d, s):
    # charges after the last shoot is useless
    s = s.rstrip("C")

    # index of last shoot
    last_s = 0
    # an array keeping the track of all charges in s
    c_idx_arr = []
    c_idx = 0
    power = 1
    current_d = 0
    for i in range(len(s)):
        if s[i] == 'S':
            last_s = i
            current_d += power
        elif s[i] == 'C':
            c_idx_arr.append(i)
            c_idx += 1
            power *= 2
            
    if current_d <= d:
        print "Case #{}: {}".format(cn, 0)
        return

    c_idx = len(c_idx_arr) - 1
    move = 0
    while c_idx >= 0:
        move += 1
        c_idx_arr[c_idx] += 1
        current_d = current_d - power / 2

        if current_d <= d:
            break
        
        if c_idx_arr[c_idx] == last_s:
            c_idx -= 1
            last_s -= 1
            power /= 2
        """
        debug = ""
        for i in range(len(s)):
            if i in c_idx_arr:
                debug += 'C'
            else:
                debug += 'S'
        print(debug)
        """

    if c_idx < 0:
        print "Case #{}: IMPOSSIBLE".format(cn)
    else:
        print "Case #{}: {}".format(cn, move)

if __name__ == "__main__":
    t = int(raw_input())
    for i in xrange(1, t + 1):
        d, s = [s for s in raw_input().split(" ")]
        solve(i, int(d), s)
        

