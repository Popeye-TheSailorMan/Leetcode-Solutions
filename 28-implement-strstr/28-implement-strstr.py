class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            arr = haystack.split(needle)
            return len(arr[0])
        else:
            return -1