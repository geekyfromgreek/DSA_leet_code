# LeetCode 412 — Fizz Buzz 
 
For the problem, we had to return an array from `1` to `n` in a string 
 
- If the number is divisible by **3 and 5** ->"FizzBuzz"` 
- If divisible by **3** -> `"Fizz"` 
- If divisible by **5** ->`"Buzz"` 
- else  return the number as a string (str(i)) 
 
So we used a **single for loop** with `if / elif / else` conditions 
 
## What is `%` (Modulo)? 
 
`%` gives the remainder after division. 
  
example: 
15 % 3 = 0 
15 % 5 = 0 
 
## Why did we check 3 and 5 first? 
 
Because a number like 15 is divisible by both 3 and 5. 
 
answer.append("Fizz") 
 
`append()` adds an element to the end of the list. 
 
# Complexity 
 
- Time: O(n) because we use one loop from 1 to n. 
- Space: O(n) because the answer array stores n elements.