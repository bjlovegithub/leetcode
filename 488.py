class Solution(object):
    def findMinStep(self, board, hand):
        """
        Just search.

        :type board: str
        :type hand: str
        :rtype: int
        """

        ballNum = {}
        for c in hand:
            if c in ballNum:
                ballNum[c] = ballNum[c] + 1
            else:
                ballNum[c] = 1

        if not self._precheck(board, ballNum):
            return -1

        return self._search(board, ballNum)

    def _precheck(self, board, num):
        # no solution if the total ball num for a specific color is less than 3.
        total = {}
        for c in board:
            if c in total:
                total[c] = total[c] + 1
            else:
                total[c] = 1

        for c in total:
            if c in num:
                total[c] += num[c]

        for k, v in total.items():
            if v < 3:
                return False

        return True
        

    def _search(self, board, num):
        availableBall = 0
        for k, v in num.items():
            availableBall += v
        if availableBall == 0 and len(board) != 0:
            return -1

        if not self._precheck(board, num):
            return -1

        start = 0
        minMoves = 1000000
        while start < len(board):
            ball = board[start]

            end = start + 1
            while end < len(board) and board[end] == ball:
                end += 1

            if ball not in num:
                start += 1
            else:
                need = 3 - (end - start)
                if need < 0:
                    need = 1
                if need > num[ball]:
                    # do nothing, search from next position with different ball
                    start = end
                else:
                    num[ball] = num[ball] - need
                    newBoard = self._compact(board, start, end)
                    if len(newBoard) != 0:
                        ret = self._search(newBoard, num)
                        if ret != -1 and minMoves > ret + need:
                            minMoves = ret + need
                    else:
                        if minMoves > need:
                            minMoves = need

                    start = end
                    
                    # resume ball num
                    num[ball] = num[ball] + need

        if minMoves == 1000000:
            return -1
        return minMoves

    def _compact(self, s, start, end):
        """
        s=AARRRYYRRA, start=5, end=7, based on the rule, all balls will be removed, so
        the compacted string is empty string.
        s=ARRRYYRA, start=4, end=7, compacted string is AA
        """
        if start == 0:
            return s[end:]

        if end == len(s):
            return s[0:start]

        start -= 1

        while start >= 0 and end < len(s):
            if s[start] != s[end]:
                break

            ball = s[start]
            num = 0
            newStart = start
            newEnd = end
            while newStart >= 0 and s[newStart] == ball:
                newStart -= 1
                num += 1

            while newEnd < len(s) and s[newEnd] == ball:
                newEnd += 1
                num += 1

            if num < 3:
                break

            start = newStart
            end = newEnd

        if start < 0:
            return s[end:]
        else:
            return s[0:start + 1] + s[end:]
            
    def test(self, s, start, end):
        return self._compact(s, start, end)

if __name__ == "__main__":
    s = Solution()

    assert 3 == s.findMinStep("GGRRGRRYY", "RYRBR")
    assert 1 == s.findMinStep("YYYYY", "RYRBR")
    assert 2 == s.findMinStep("WWRRBBWW", "WRBRW")
    assert -1 == s.findMinStep("WRRBBW", "RB")
    assert 2 == s.findMinStep("WRRBBWW", "RB")
