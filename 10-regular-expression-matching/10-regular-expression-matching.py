import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # if ('*'in p or '.' in p):
        #     x = re.search(p,s)
        #     return x
        pattern = ('^'+p+'$')
        return re.match(pattern,s)