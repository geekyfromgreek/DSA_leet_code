class Solution:
     def reverse(self, x):
            ld= 0
            reversed=0
            pos=1
            neg=-1
            if x >= 0:
             sign =pos
            else:
                sign=neg
                x= abs(x)
            while x != 0: 
              ld= x % 10
              reversed= reversed * 10 + ld
              x =  x // 10
            reversed = reversed*sign

            if  reversed < -2**31 or  reversed > 2**31-1:
              return 0
            else:
              return reversed
