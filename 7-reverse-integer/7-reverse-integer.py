class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            sign = -1
            x = x*-1
        else:
            sign = 1
        if (x<(2**31)):
            string = str(x)
            string = string[::-1]
            s = int(string)
            if (s<(2**31)):
                return (s*sign)
        return 0
        
        