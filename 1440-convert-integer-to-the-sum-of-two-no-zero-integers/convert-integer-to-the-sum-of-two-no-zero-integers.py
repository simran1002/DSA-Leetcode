class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for  a in range(1,n):
            b=n-a
            if '0' not in str(b) and '0' not in str(a):
                return [a,b]

            
        