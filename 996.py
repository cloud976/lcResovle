from math import sqrt
from math import ceil
class Solution(object):
    co = 0
    def isSquare(self, num):
        numSqrt = sqrt(num)
        if (ceil(numSqrt) == numSqrt):
            return True
        return False
    def isSquareList(self, A):
        for i in range(len(A)-1):
            if (not (self.isSquare(A[i]+A[i+1]))):
                return False
        return True
    def unique(self, list):
        newlist = []
        for x in list:
            if x not in newlist:
                newlist.append(x)
        return newlist
    def fullList(self, A, lastNum):
        retList = []
        if len(A) == 2:
            return [[A[0], A[1]] ,[A[1], A[0]]]
        uniqList = self.unique(A)
        for a in uniqList:
            tmpList = list(A)
            tmpList.remove(a)
            if lastNum>0 and (not self.isSquare(lastNum+a)):
                continue
            for oneList in self.fullList(tmpList, a):
                self.co = self.co+1
                if (not self.isSquare(a + oneList[0])):
                    continue
                retList.append([a]+oneList)
        return retList
    def numSquarefulPerms(self, A):
        co = 0
        for lst in self.unique(self.fullList(A, -1)):
            if self.isSquareList(lst):
                co = co+1
        return co
so = Solution()
print(so.numSquarefulPerms([0,0,0,1,1,1]))
print(so.co)