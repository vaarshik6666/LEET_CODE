class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            x = int(str(x)[::-1]) 
        else:
            x = -1*x
            x = -1*int(str(x)[::-1])
        if x < (2**31)-1 and x > -(2**31):
            return x
        else:
            return 0