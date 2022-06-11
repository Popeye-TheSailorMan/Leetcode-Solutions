class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = str(x)
        rev = rev[::-1]
        if (str(x) == rev):
            return True
        return False