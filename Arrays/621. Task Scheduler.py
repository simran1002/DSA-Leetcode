'''
You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. 
Each cycle or interval allows the completion of one task. Tasks can be completed in any order,
 but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.
​Return the minimum number of intervals required to complete all tasks.
'''

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        if len(tasks)==1:
            return 1
        dic = Counter(tasks)
        
        vals = list(dic.values())
        t = max(vals)

        time = (t-1) * (n+1) + 1
        for i in range(0, len(vals)):
            if vals[i]==t:
                time += 1
        return max(time-1, len(tasks))
    

# Time Complexity: O(n)
# Space Complexity: O(1)