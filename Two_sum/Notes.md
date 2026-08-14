# First Approach using Brute Force Approach

for the problem, we had to find the sum of  the two elements in the array, such that it matches the target value, each element can be used only once
so we used Brute Force Approach

**But what is Brute Force Approach?**
  its basically using all of the combinations until u ran out of options
 for it we used nested for loops and iterated through each element until sum matched our integer value target
 
  but...it has O(n2) complexity

**what is  self?**

self is  current object
 so u create object  like
 sol1=solution()
and use
sol1.twoSum() , python passes sol1 as self and method gets executed

if we don use self, python still sends sol1 as argument but sol1 is not the expected parameter in function, so it gives typerror


# Second Approach using Hash Map Approach

for the problem, instead of checking all the combinations like Brute Force, we can remember the elements we have already seen using a Hash Map.

**But what is Hash Map?**

Hash Map basically stores data in key → value form.

In Python, we use a dictionary as a Hash Map.

For our problem, we store:

number → index

for example:
needed= target - nums[i]
here needed becomes 9-2=7,
 we havent seen 7 before, so store it (seen[nums[i]=i)
here we save 7 as 7,0
then comes 7, needed=9-7
we have seen 2 before, its in hash map so, if needed is in seen,
 we return seen of needed, that is seen of 2, and i, which is 1 currently