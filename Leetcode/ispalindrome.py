class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            return str(x) == str(x)[::-1]
        else:
            return False
        
# 3ms Beats88.48%
# 17.71MB Beats63.84%



# Suggested Alternative
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reverse = 0
        xcopy = x

        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x //= 10
        
        return reverse == xcopy