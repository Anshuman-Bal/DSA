from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        s_freq = defaultdict(int)
        t_freq = defaultdict(int)

        for c in s:
            s_freq[c] = s_freq[c] + 1
        for c in t:
            t_freq[c] = t_freq[c] + 1

        if s_freq == t_freq:
            return True

        return False
    
if __name__ == "__main__":

    s = "cat"
    t = "rat"

    sol_instance = Solution()
    print(sol_instance.isAnagram(s=s, t=t))