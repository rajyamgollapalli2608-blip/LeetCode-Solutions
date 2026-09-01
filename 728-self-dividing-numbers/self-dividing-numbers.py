class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l = []

        for i in range(left, right + 1):
            nums = i
            valid = True

            while i > 0:
                r = i % 10

                if r == 0:
                    valid = False

                elif nums % r != 0:
                    valid = False

                i = i // 10

            if valid:
                l.append(nums)

        return l