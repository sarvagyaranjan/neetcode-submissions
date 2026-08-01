class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict

        left = 0
        right = 0 
        hashmap = defaultdict(int)
        ans = 0 
        for right in range(len(s)): 
            hashmap[s[right]]+=1

            while hashmap[s[right]]>1: 
                hashmap[s[left]]-=1
                left+=1
            ans = max(ans, right - left + 1)
        return ans 