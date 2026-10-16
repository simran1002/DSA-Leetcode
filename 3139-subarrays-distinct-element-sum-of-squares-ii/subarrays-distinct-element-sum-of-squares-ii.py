class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self.sum_val = [0] * (4 * n)
        self.MOD = 10**9 + 7

    def update(self, node, start, end, l, r, val, MOD):
        if r < start or end < l:
            return
        if l <= start and end <= r:
            length = (end - start + 1)
            self.tree[node] = (self.tree[node] + 2 * self.sum_val[node] * val + val * val * length) % MOD
            self.sum_val[node] = (self.sum_val[node] + val * length) % MOD
            self.lazy[node] = (self.lazy[node] + val) % MOD
            return
        
        mid = (start + end) // 2
        self.push_down(node, start, end, mid, MOD)
        self.update(2 * node, start, mid, l, r, val, MOD)
        self.update(2 * node + 1, mid + 1, end, l, r, val, MOD)
        self.tree[node] = (self.tree[2 * node] + self.tree[2 * node + 1]) % MOD
        self.sum_val[node] = (self.sum_val[2 * node] + self.sum_val[2 * node + 1]) % MOD

    def push_down(self, node, start, end, mid, MOD):
        lz = self.lazy[node]
        if lz != 0:
            left, right = 2 * node, 2 * node + 1
            
            l_len = (mid - start + 1)
            self.tree[left] = (self.tree[left] + 2 * self.sum_val[left] * lz + lz * lz * l_len) % MOD
            self.sum_val[left] = (self.sum_val[left] + lz * l_len) % MOD
            self.lazy[left] = (self.lazy[left] + lz) % MOD

            r_len = (end - mid)
            self.tree[right] = (self.tree[right] + 2 * self.sum_val[right] * lz + lz * lz * r_len) % MOD
            self.sum_val[right] = (self.sum_val[right] + lz * r_len) % MOD
            self.lazy[right] = (self.lazy[right] + lz) % MOD

            self.lazy[node] = 0

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        tree = SegmentTree(n)
        last_seen = {}
        total_sum = 0

        for r in range(n):
            x = nums[r]
            l = last_seen.get(x, -1) + 1
            
            tree.update(1, 0, n - 1, l, r, 1, MOD)
            last_seen[x] = r
            
            total_sum = (total_sum + tree.tree[1]) % MOD

        return total_sum