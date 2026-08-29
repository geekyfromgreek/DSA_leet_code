class Solution:
    def reverseString(self, s) :
            left=0
            right=len(s)-1
            def helper(s,left,right):
    
                if left >= right:
                     return 
                s[left],s[right] =s[right],s[left]
                helper(s,left+1,right-1)
            helper(s,0,len(s)-1)