class Solution:
    def isPalindrome(self, x: int) -> bool:
        x= str(x)
        k=x[::-1]
        if x==k:
            return True
        else:
            return False
