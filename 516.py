class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        matrix = []
        length = len(s)
        for i in range(length):
            matrix.append([0 for i in range(length + 1)])
        
        for i in range(len(matrix)):
            matrix[i][1] = 1

        # dp
        ret = 1
        for subLen in range(2, length + 1):
            for start in range(length - subLen + 1):
                if s[start] == s[start + subLen - 1]:
                    matrix[start][subLen] = matrix[start + 1][subLen - 2] + 2
                else:
                    matrix[start][subLen] = max(matrix[start + 1][subLen - 1], matrix[start][subLen - 1])

                if ret < matrix[start][subLen]:
                    ret = matrix[start][subLen]

        return ret

if __name__ == "__main__":
    sol = Solution()
    
    print sol.longestPalindromeSubseq("cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc")
    #print sol.longestPalindromeSubseq("bbbab")
