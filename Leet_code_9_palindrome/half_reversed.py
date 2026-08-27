class Solution:
    def isPalindrome(self, x):
          revnum=0
          palindrome=x
          if x<0  or x!=0 and x%10==0:
             return False
          while x>revnum:
                lastdigit=x % 10
                revnum=revnum*10 + lastdigit
                x=x//10
          return  x==revnum or x==revnum//10
