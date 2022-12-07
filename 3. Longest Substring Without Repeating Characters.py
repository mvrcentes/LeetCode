class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = ""
        max = 0
    
        for i in range(len(s)):
            if s[i] != s[i + 1:] and s[i] not in temp:
                temp += s[i]
                if len(temp) > max:
                    max = len(temp)
            else:
                oldtem = temp.find(s[i])
                temp = temp[oldtem+ 1:] + s[i]
 
        return max
            
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))