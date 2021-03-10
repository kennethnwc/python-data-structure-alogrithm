# range sum
from typing import List
class SegmentTree:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (self.n << 1)
        for i in range(self.n):
            self.tree[i + self.n] = nums[i]
        
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]
        
        
    def update(self, i: int, val: int) -> None:
        i += self.n
        self.tree[i] = val
        while i > 0:
            self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
            i >>= 1
        
        
    def sum_range(self, i: int, j: int) -> int:
        # [i , j]
        i += self.n
        j += self.n + 1
        res = 0
        while i < j:
            if i & 1:
                res += self.tree[i]
                i += 1
            if j & 1:
                j -= 1
                res += self.tree[j]
            
            i >>= 1
            j >>= 1
        return res


a = SegmentTree([1,3,5])
a.sum_range(0, 2)
a.update(0, 2)
a.sum_range(0, 2)
