class Solution:

    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        s = s.lower()

        while right > left:

            if not s[left].isalnum():
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue

            if not s[left] == s[right]:
                return False

            if s[left] == s[right]:
                left += 1
                right -= 1

        return True


s = Solution()

print(s.isPalindrome("A man, a plan, a canal: Panama"))
