class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        left = 0
        right = 0 
        ans = []

        for right in range(len(nums)): 

            if right - left + 1 ==k : 
                maxi = max(nums[left: right + 1])
                ans.append(maxi)
            
                left+=1
        
        return ans

        