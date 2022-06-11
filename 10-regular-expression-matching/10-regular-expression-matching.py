import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern = ('^'+p+'$')
        return re.match(pattern,s)