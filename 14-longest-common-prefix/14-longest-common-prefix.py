class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        length = 0
        res = ""
        for word in strs:
            if(len(word) > length):
                length = len(word)
        for word in strs:
            if(len(word) < length):
                length = len(word)
        curr = ""
        counter = 0
        for word in strs:
            if word == "":
                return  ""
        while i<length:
            
            for j in range(0,len(strs)):
                curr = strs[0][i]
                if (strs[j][i]!= curr):
                    return res
            res+=curr
            i+=1
        return res