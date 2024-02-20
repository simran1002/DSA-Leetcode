'''
There are n couples sitting in 2n seats arranged in a row and want to hold hands.
The people and seats are represented by an integer array row where row[i] is the ID of the person sitting in the ith seat.
The couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2n - 2, 2n - 1).
Return the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, 
then they stand up and switch seats.
'''

class Solution:
    def minSwapsCouples(self, row: list[int]) -> int:
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY

        n = len(row) // 2
        parent = [i for i in range(n)]
        
        for i in range(0, len(row), 2):
            union(row[i] // 2, row[i+1] // 2)
        
        count = sum([1 for i, x in enumerate(parent) if i == find(x)])
        return n - count
    
# Time complexity: O(n)
# Space complexity: O(n)