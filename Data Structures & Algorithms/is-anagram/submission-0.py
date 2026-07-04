class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        s_hashmap = {}
        t_hashmap = {}

        for i in s:
            if i not in s_hashmap:
                s_hashmap[i] = 1
            else:
                s_hashmap[i]+=1
            
        for i in t:
            if i not in t_hashmap:
                t_hashmap[i] = 1
            else:
                t_hashmap[i]+=1

        return t_hashmap == s_hashmap
        