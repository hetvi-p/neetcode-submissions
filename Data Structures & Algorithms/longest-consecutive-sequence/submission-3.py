class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        res = 0
        present = set(nums)

        for n in nums:
            count, cur = 0, n
            if n-1 not in present:
                while cur in present:
                    count += 1
                    cur = cur + 1
            res = max(res, count)

        return res
        
            


