from typing import List
class Solution:
    def findRelativeRanks(self, scores: List[int]) -> List[str]:
        sorted_scores = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
        result = [""] * len(scores)
        for rank, (index, score) in enumerate(sorted_scores):
            if rank == 0:
                result[index] = "Gold Medal"
            elif rank == 1:
                result[index] = "Silver Medal"
            elif rank == 2:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(rank + 1)  
        return result