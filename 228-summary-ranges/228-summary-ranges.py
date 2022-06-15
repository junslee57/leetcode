class Solution(object):
    def summaryRanges(self, nums):
        
        if len(nums) == 0:
            return []
            
        summary = []
        
        start = nums[0]
        end = nums[0]
        
        for num in nums[1:]:
            if end + 1 != num:
                if start == end:
                    summary.append(str(start))
                else:
                    summary.append(str(start) + "->" + str(end))
                start = num
                end = num
            else:
                end = num
        if start == end:
            summary.append(str(start))
        else:
            summary.append(str(start) + "->" + str(end))
            
        return summary