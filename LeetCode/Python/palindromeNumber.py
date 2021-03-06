class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revertedNum = 0
        while (x > revertedNum):
            revertedNum = (revertedNum * 10) + x % 10
            x //= 10
        
        return revertedNum == x or revertedNum // 10 == x