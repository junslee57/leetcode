class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        cnt , mx = 0, 0
        for data in nums : 
            if(data) : 
                cnt += 1
            else : 
                cnt = 0
            mx = max(mx,cnt)
        return mx