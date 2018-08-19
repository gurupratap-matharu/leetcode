
class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([reverseString(word) for word in s.split(' ')])


def reverseString(s):
    """
    Returns the reverse of a string
    """
    s = list(s)
    s.reverse()
    s = ''.join(s)
    return s
