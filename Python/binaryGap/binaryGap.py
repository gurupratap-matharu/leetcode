class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        distance = 0  # initiate default distance
        lst = [0]  # we store all the distances found here.
        n = bin(N)[2:]  # Since python returns binary value in a string format starting with '0b'
        for char in n[1:]:
            distance += 1
            if char == '1':
                lst.append(distance)
                distance = 0
        return max(lst)


solution = Solution()
print(solution.binaryGap(8))
