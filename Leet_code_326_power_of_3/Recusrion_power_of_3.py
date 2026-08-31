class Solution:
    def isPowerOfThree(self, n) :
            if n<=0 :
                return False
            if n==1:
             return True

            if not n% 3==0:
                return False
            
            return self.isPowerOfThree(n//3)
     