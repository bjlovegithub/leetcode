import heapq

class Boat(object):
    def __init__(self, limit):
        self.passengers = 0
        self.left = limit

    def __cmp__(self, other):
        return self.left < other.left

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort(reverse=True)

        boats = []
        boatNum = 0

        m = {}
        for p in people:
            if p in m:
                m[p] = m[p] + 1
            else:
                m[p] = 1

        for p in people:
            #print p, m[p], len(boats)
            if m[p] == 0:
                continue
            if len(boats) == 0:
                boat = Boat(limit)
                boatNum += 1
            else:
                boat = heapq.heappop(boats)

            if boat.left >= p:
                boat.left -= p
                boat.passengers += 1
                m[p] = m[p] - 1

                if boat.passengers < 2:
                    if boat.left in m and m[boat.left] > 0:
                        # do not put it back to heap
                        m[boat.left] = m[boat.left] - 1
                    elif boat.left > 0:
                        heapq.heappush(boats, boat)
            else:
                if boat.left in m and m[boat.left] > 0:
                    m[boat.left] = m[boat.left] - 1
                else:
                    heapq.heappush(boats, boat)
                    boat = Boat(limit)
                    boat.left -= p
                    m[p] = m[p] - 1
                    boat.passengers += 1
                    boatNum += 1
                    
                    if boat.left in m and m[boat.left] > 0:
                        m[boat.left] = m[boat.left] - 1
                    elif boat.left > 0:
                        heapq.heappush(boats, boat)
          
        return boatNum

if __name__ == "__main__":
    s = Solution()
    print s.numRescueBoats([3,2,3,2,2], 6)
