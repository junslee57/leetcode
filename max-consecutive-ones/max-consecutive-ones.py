class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        res = 0
        while(nums):
            i = nums.pop()
            if i == 1:
                cnt += 1
            else:
                if res < cnt:
                    res = cnt
                cnt = 0
        if res < cnt:
            return cnt
        return res