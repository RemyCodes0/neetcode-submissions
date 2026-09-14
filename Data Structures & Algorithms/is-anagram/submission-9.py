class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = {}
        t_freq = {}

        for char in  s:
            if char not in s_freq:
                s_freq[char] = 0
            else:
                s_freq[char]+=1
        for char in t:
            if char not in t_freq:
                t_freq[char] = 0
            else:
                t_freq[char]+=1

        if s_freq == t_freq:
            return True
        else:
            return False
                       
