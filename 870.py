class Solution(object):
    def find(self, A, num):
        start = 0
        end = len(A) - 1
        mid = (start+end)/2
        while start < end:
            obj = A[mid]
            if obj > num:
                end = mid
            else:
                start = mid + 1
            mid = (start+end)/2
        return mid
        
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A.sort()
        BB = [(B[idx], idx) for idx in range(len(B))]
        BB.sort(key = lambda x : x[0])
                
        result = [i for i in range(len(A))]
        for idx in range(len(BB)):
            mid = self.find(A, BB[idx][0])
            result[BB[idx][1]] = A[mid]
            del A[mid]
        return result
