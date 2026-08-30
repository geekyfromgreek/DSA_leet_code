class Solution:
    def isPalindrome(self, s: str) -> bool:

        def helper(left, right):

            if left>=right:
              return True
              
            if not s[left].isalnum():
                return helper(left + 1, right)

            if not s[right].isalnum():
                return helper(left, right - 1)

            if s[left].lower() != s[right].lower():
                return False

            return helper(left + 1, right - 1)

        return helper(0, len(s) - 1)