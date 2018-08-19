class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        s.reverse()
        s = ''.join(s)
        return s


sol1 = Solution()
print(sol1.reverseString("Inderpal Singh Matharu"))
