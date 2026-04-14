class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        product = 1

        pre = []
        suf = [0] * (len(nums))

        prod = 1
        for n in nums:
            pre.append(prod)
            prod = prod * n

        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            suf[i] = prod
            prod = prod * nums[i]
        
        res = []

        for i in range(len(nums)):
            res.append(pre[i] * suf[i])

        return res

        [1, 1, 2, 8]
        [48, 24, 6, 1]




        
        

        return res
            


        