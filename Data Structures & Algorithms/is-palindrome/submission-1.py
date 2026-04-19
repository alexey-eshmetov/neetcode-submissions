class Solution:
    def isPalindrome(self, s: str) -> bool:
        mod = s.lower().replace(" ","")
        mod = "".join(filter(str.isalpha, mod))
        for char in s:
            if char.isdigit():
                return False
        if mod == mod[::-1]:
            return True
        else:
            return False