class Solution:
    def isPalindrome(self, x: int) -> bool:

        org_num = x

        if x < 0:
            return False

        res = 0

        while x != 0:

            last_digit = x % 10
            x = x // 10
            res = res * 10 + last_digit

        if res == org_num:
            return True
        else:
            return False


s = Solution()
#
print(s.isPalindrome(121))
