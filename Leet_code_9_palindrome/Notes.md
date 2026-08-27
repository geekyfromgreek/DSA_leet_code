````md
# LeetCode 9 — Palindrome Number

For the problem, we had to check whether a number is a **palindrome**.

A palindrome is a number that stays the same when reversed.

Example:

121 → 121 → Palindrome

## Approach 1 — Reverse Full Number

- Store the original number.
- Use `% 10` to get the last digit.
- Use `// 10` to remove the last digit.
- Build the reversed number using `revnum * 10 + lastdigit`.
- Compare the reversed number with the original number.

Example:

```text
121

1 → revnum = 1
2 → revnum = 12
1 → revnum = 121

121 == 121 → True
````

## Approach 2 — Reverse Half

Instead of reversing the whole number, reverse only the **second half** and compare it with the first half.

* Use `revnum = 0`.
* Keep taking the last digit from `x`.
* Use `while x > revnum` to stop around the middle.
* For even digits → `x == revnum`.
* For odd digits → `x == revnum // 10`.

Example:

```text
1221

x = 12
revnum = 12

12 == 12 → True
```

For an odd number:

```text
12321

x = 12
revnum = 123
```

The `3` is the **middle digit**, so it doesn't need to be checked.

```text
123 // 10 = 12

12 == 12 → True
```

## Important Edge Cases

* Negative numbers → `False`
* Number ending in `0` → `False`, except `0` itself
* `0` → `True`

## New Things Learned

* `% 10` → gets the last digit.
* `// 10` → removes the last digit.
* `revnum * 10 + lastdigit` → builds the reversed number.
* In a palindrome, the middle digit of an odd-length number can be anything.
* Half reversal avoids reversing the complete number.

## Complexity

### Approach 1

* Time: O(log₁₀ n)
* Space: O(1)

### Approach 2

* Time: O(log₁₀ n)
* Space: O(1)
* Processes only about half the digits.

```
```