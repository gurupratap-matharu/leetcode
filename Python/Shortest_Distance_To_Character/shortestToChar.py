class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        self.string = list(S)
        self.char = C

        lst = [abs(x-self.string.index(self.char)) for x in range(len(self.string))]

        while True:
            try:

                distance = self.string.index(self.char)

                for i in range(len(self.string)):
                    if abs(i-distance) < lst[i]:
                        lst[i] = abs(i-distance)

                self.string[distance] = '#'

            except ValueError:

                break
        return lst


