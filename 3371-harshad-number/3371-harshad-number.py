class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        result = 0
        temp = x
        while temp != 0:
            num = temp % 10
            result += num
            temp //= 10
        if x % result == 0:
            return result
        else:
            return -1