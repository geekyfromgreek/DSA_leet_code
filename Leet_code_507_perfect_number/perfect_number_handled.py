class Solution:
    def checkPerfectNumber(self, num) :
        sum=0
        for i   in range (1, int(num**0.5 )+ 1):
             if num % i==0:
              sum=sum + i
                  
              if num//i!=i and  num // i !=num :
                    sum= sum  +num//i
        if  sum == num :
              if num ==1:
               return False
              else:
                return  True
        else:
            return False