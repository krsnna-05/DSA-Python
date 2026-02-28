class Solution:
    def isArmstrong(self, n: int):

        if n < 0:
            return False

        org_num = n
        res = 0
        num_len = len(str(org_num))

        while n != 0:
            last_digit = n % 10
            n = n // 10

            res = res + last_digit**num_len

        return res == org_num


s = Solution()

print(s.isArmstrong(153))
