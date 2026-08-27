class Solution:
    def isPalindrome(self, x):
          revnum=0
          palindrome=x
          while x>0 :
                lastdigit=x % 10
                revnum=revnum*10 + lastdigit
                x=x//10
          return  revnum==palindrome
