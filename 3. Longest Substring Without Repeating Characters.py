class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        rtype = 0
        temp = ""
        max = 0
        for i in s:
            if i not in temp:
                temp += i
                rtype += 1

        for i in range(len(s)):
            if s[i] != s[i + 1:] and s[i] not in temp:
                temp += s[i]
                rtype += 1
                    
            elif s[i] in temp: 
                temp = ""
                rtype = 0
            else:
                break
        return rtype
            
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))