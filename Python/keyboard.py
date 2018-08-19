class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        top, mid, bottom = set('qwertyuiop'), set('asdfghjkl'), set('                                zxcvbnm')
        answer = []
        for word in words:
            w = set(word.lower())
            if w.issubset(top) or w.issubset(mid) or w.issubset(bottom):
                answer.append(word)

        return answer


a = Solution()
print(a.findWords(["Hello", "Alaska", "Dad", "Peace"]))
