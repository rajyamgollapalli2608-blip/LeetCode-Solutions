class Solution:
    def reverseDegree(self, s: str) -> int:
        summ = 0

        for i in range(len(s)):
            position = ord(s[i]) - ord('a') + 1
            reverse_position = 27 - position
            summ += reverse_position * (i + 1)

        return summ