class Solution(object):
    def __init__(self):
        self.maxLen = 0
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        pointsCount = len(points)
        samePoint = 0
        if pointsCount < 1:
            self.maxLen = 0
        elif pointsCount == 1:
            self.maxLen = 1
        if pointsCount == 2:
            self.maxLen = 2
        else:
            for i in range(pointsCount):
                pt1 = points[i]
                samePoint = 0
                for n in range(i+1, pointsCount):
                    pt2 = points[n]
                    if pt1 == pt2:
                        samePoint+=1
                        continue
                    maxLen = 2
                    linear = self.getLineEquation(pt1, pt2)
                    for m in range(n+1, pointsCount):
                        if linear(points[m]):
                            maxLen+=1
                    maxLen+=samePoint
                    if maxLen > self.maxLen:
                        self.maxLen = maxLen
            if self.maxLen == 0:
                self.maxLen = pointsCount
        return self.maxLen
        
    def getLineEquation(self, pointA, pointB):
        if pointA[0] == pointB[0] and pointA[1] == pointB[1]:
            return lambda pointC: True
        return lambda pointC:  (pointB[1]-pointA[1]) * pointC[0] + (pointA[0]-pointB[0]) * pointC[1] + (pointB[0]*pointA[1] - pointA[0]*pointB[1]) == 0
    


so = Solution()

print so.maxPoints([[1,1],[1,1],[2,3]])
