class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        res = 0
        present = set(nums)

        for n in present:

            if n-1 not in present:
                length = 1
                while (n + length) in present:
                    length += 1
                res = max(res, length)

        return res
        
            


