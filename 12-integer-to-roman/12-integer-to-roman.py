class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        numerals : (str,int) = [
            ("M",1000),
            ("CM",900),
            ("D", 500),
            ("CD", 400),
            ("C", 100),
            ("XC",90),
            ("L",50),
            ("XL", 40),
            ("X",10),
            ("IX",9),
            ("V",5),
            ("IV",4),
            ("I",1)
        ]
        
        for symbol, nums in numerals:
            res+=(num//nums)*symbol
            num%=nums
        return res