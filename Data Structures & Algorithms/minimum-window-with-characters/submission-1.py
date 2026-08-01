def valid(need, window):
    for i in need: 
        if window[i] < need[i]: 
            return False
    return True 

class Solution:


    def minWindow(self, s: str, t: str) -> str:

        from collections import defaultdict

        left = 0 
        right = 0
       

        hash_1 = defaultdict(int)
        hash_2 = defaultdict(int)
        ans = ""

        min_len = float('inf')

        for i in t: 
            hash_1[i]+=1
        
        for right in range(len(s)): 
            hash_2[s[right]]+=1
        

            while valid(hash_1, hash_2):

                if right - left + 1 < min_len: 
                    min_len = right - left + 1
                    ans = s[left: right + 1]
                
                hash_2[s[left]]-=1
                if hash_2[s[left]] == 0: 
                    del hash_2[s[left]]
                left+=1
        return ans


            