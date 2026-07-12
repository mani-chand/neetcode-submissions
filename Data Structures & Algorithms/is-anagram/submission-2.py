class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            s_dict[s[i]] = s_dict.get(s[i],0)+1
            t_dict[t[j]] = t_dict.get(t[j],0)+1
            i += 1
            j += 1
        while i < len(s) and j < len(t):
            s_dict[s[i]] = s_dict.get(s[i],0)+1
            i += 1
        while i < len(s) and j < len(t):
            t_dict[t[j]] = t_dict.get(t[j],0)+1
            j += 1
        for ele in t:
            if ele not in s or s_dict[ele] != t_dict[ele]:
                return False
        return True
        


        
        
        