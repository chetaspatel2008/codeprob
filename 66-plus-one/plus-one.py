class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        number = int("".join(map(str, digits)))
        number += 1
        lis = [int(digi) for digi in str(number)]
        return lis