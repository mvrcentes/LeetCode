class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rtype = ""
        st = 0 
        st_count = 0
        
        i = 0
        i_ = 0

        while st < len(s):
            for j in range(len(s)):
                i += i_
                i += j
                if s[st:(i + 1)] == s[i::-1] or s[st:(i + 1)] == s[i - len(s):(st - 1):-1]:
                    if len(s[st:(i + 1)]) > st_count:
                        rtype = s[st:(i + 1)]
                        st_count = len(s[st:(i + 1)])
                        i = 0
                else:
                    i = 0
            st += 1
            i_ += 1
        return rtype


word = Solution()
print(word.longestPalindrome("cbbd"))

#Tengo que entender como funciona del todo

def longestPalindrome(s):
        start = 0
        longest_pal_count = 0
        longest_pal = ''
        i = 0
        const_i = 0
        while start < len(s):
            for j in range(len(s)):
                i += const_i
                i += j
                if s[start:(i+1)] == s[i:None:-1] or s[start:(i+1)] == s[i-len(s):(start-1):-1]:
                    if len(s[start:(i+1)]) > longest_pal_count:
                        longest_pal = s[start:(i+1)]
                        longest_pal_count = len(s[start:(i+1)])
                        i = 0
                else:
                    i = 0
            start += 1
            const_i += 1
        return(longest_pal)

print(longestPalindrome("cbbd"))
