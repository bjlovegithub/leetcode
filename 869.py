import math

class Solution(object):
    def isUnique(self, arr, depth, usedMap, N, P, okMap, checkedPrefix):
        if depth == len(arr):
            base = math.log(N, 2)
            if base == int(base):
                okMap[N] = 1
            return
       
        for i in range(len(arr)):
            if depth == 0 and arr[i] == 0:
                continue
            if not usedMap[i]:
                usedMap[i] = True
                prefix = arr[i] * P + N
                if prefix not in checkedPrefix:
                    self.isUnique(arr, depth + 1, usedMap, prefix, P / 10, okMap, checkedPrefix)
                    checkedPrefix[prefix] = True
                usedMap[i] = False

                if len(okMap) > 1:
                    break
        
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        digits = []
        n = N
        p = 1
        while n > 0:
            digits.append(n % 10)
            n /= 10
            if n > 0:
                p *= 10

        okMap = {}
        usedMap = {}
        for i in range(len(digits)):
            usedMap[i] = False
        self.isUnique(digits, 0, usedMap, 0, p, okMap, {})
        if len(okMap) == 1:
            return True
        return False

if __name__ == "__main__":
    s = Solution()
    print s.reorderedPowerOf2(679213508)
