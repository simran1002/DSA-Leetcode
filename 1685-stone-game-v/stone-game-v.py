from functools import cache
from itertools import accumulate
from typing import List


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        prefix = list(accumulate(stoneValue, initial=0))

        @cache
        def dfs(left: int, right: int) -> int:
            if left == right:
                return 0

            best = 0
            left_sum = 0
            right_sum = prefix[right + 1] - prefix[left]

            for k in range(left, right):
                left_sum += stoneValue[k]
                right_sum -= stoneValue[k]

                if left_sum < right_sum:
                    if best >= 2 * left_sum:
                        continue

                    best = max(
                        best,
                        left_sum + dfs(left, k)
                    )

                elif left_sum > right_sum:
                    if best >= 2 * right_sum:
                        break

                    best = max(
                        best,
                        right_sum + dfs(k + 1, right)
                    )

                else:
                    best = max(
                        best,
                        left_sum + dfs(left, k),
                        right_sum + dfs(k + 1, right)
                    )

            return best

        return dfs(0, len(stoneValue) - 1)