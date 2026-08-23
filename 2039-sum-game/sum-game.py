class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        left_sum = right_sum = 0
        left_q = right_q = 0

        for i, ch in enumerate(num):
            if ch == '?':
                if i < half:
                    left_q += 1
                else:
                    right_q += 1
            else:
                if i < half:
                    left_sum += int(ch)
                else:
                    right_sum += int(ch)

        q_diff = left_q - right_q
        diff = left_sum - right_sum

        if q_diff % 2 != 0:
            return True

        return diff != 9 * (right_q - left_q) // 2