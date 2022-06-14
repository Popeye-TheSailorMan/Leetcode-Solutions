class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if (digits!=""):
            let = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
            digit = [i for i in digits] 
            res = []
            ans = []
            for i in digit:
                if(int(i)!=1):
                    word = [j for j in let[int(i)]]
                    if(len(digit)==1):
                        return word
                    elif(len(digit)>1 and res == []):
                        res.extend(word)    
                    else:
                        for j in range(0,len(res)):
                            k=0
                            while k<len(word):
                                ans.append(res[j]+word[k])
                                k=k+1
                        res = ans
            result = []
            for i in range(0,len(res)):
                if (len(res[i])==len(digits)):
                    result.append(res[i])
            return result
        
        return []
                     