class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        left = 0 
        right = 0

        from collections import defaultdict

        hash_1 = defaultdict(int)
        hash_2 = defaultdict(int)

        for i in s1: 
            hash_1[i]+=1
        
        for right in range(len(s2)): 
            hash_2[s2[right]]+=1

            if right - left + 1 > len(s1): 
                hash_2[s2[left]]-=1

                if hash_2[s2[left]]==0: 
                    del hash_2[s2[left]]
                left+=1
        
            if right - left + 1 == len(s1) and hash_1 == hash_2: 
                return True
        
        return False
