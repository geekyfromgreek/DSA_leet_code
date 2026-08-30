class Solution:
    def isPalindrome(self, s: str) -> bool:
           
        left=0
        right=len(s)-1
        
        while left<right:
            if  not s[left].isalnum() :
                left=left+1
                continue
            
            if not s[right].isalnum():
                right=right-1
                continue
             
            if s[left].lower()!=s[right].lower():
                return False
            left= left+1
            right=right-1 
        return True
