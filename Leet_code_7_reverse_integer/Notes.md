# LeetCode 7 — Reverse Integer

For the problem, we had to **reverse the digits of an integer**.

- Positive → reverse normally
- Negative → preserve the `-` sign
- If the reversed number is outside the **32-bit signed integer range** → return `0`

## What I Did

- Used `% 10` to get the last digit.
- Used `// 10` to remove the last digit.
- Used `reversed * 10 + ld` to build the reversed number.
- Used a `while` loop to process all digits.
- Handled negative numbers by storing the sign separately and using `abs()` on `x`.
- Applied the sign after reversing.
- Checked whether the final reversed number is within the 32-bit range.

## What Was New

- Handling **negative numbers** while reversing.
- Understanding and checking the **32-bit signed integer range**:
  `-2³¹ to 2³¹ - 1`
- Learned that `**` is used for power in Python, while `^` is XOR.

# Complexity

- **Time:** O(log n) — each digit is processed once.
- **Space:** O(1) — only a few variables are used.