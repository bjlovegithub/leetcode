class Solution(object):
    def getDigits(self, n):
        digits = {}
        while n > 0:
            d = n % 10
            if d in digits:
                digits[d] = digits[d] + 1
            else:
                digits[d] = 1
            n /= 10

        return digits

    def check(self, m1, m2):
        if len(m1) != len(m2):
            return False

        for k in m1:
            if k not in m2 or m1[k] != m2[k]:
                return False

        return True
        
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        digits = self.getDigits(N)
        num = len(str(N))

        p2Map = {}
        start = 1
        while True:
            l = len(str(start))
            if l > num:
                break
            if l == num:
                p2Map[start] = start
            start = start * 2

        for p2 in p2Map:
            p2Digits = self.getDigits(p2)

            if self.check(digits, p2Digits):
                return True

        return False

if __name__ == "__main__":
    s = Solution()
    print s.reorderedPowerOf2(3)
