# LeetCode 1929 — Concatenation of Array 
 
For the problem, we had to create an array `ans` of length `2n` where `ans` is the concatenation of two `nums` arrays.

Example:

`nums = [1, 2, 3]`

`ans = [1, 2, 3, 1, 2, 3]`

## First Approach using For Loops

We created an empty `ans` array and used two separate `for` loops.

- First loop → adds the first copy of `nums`
- Second loop → adds the second copy of `nums`

## Second  Approach using concatination

Python supports concatination of list so we just use + operator and return ans