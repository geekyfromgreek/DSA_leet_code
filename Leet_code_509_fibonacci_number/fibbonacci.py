class Solution:
    def fib(self, n):
      if n<=1:
       return n
        
      secondlast= self.fib(n-2)
      last= self.fib(n-1)
        
      return last + secondlast
        