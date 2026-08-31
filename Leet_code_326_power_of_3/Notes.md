# Power of Three — Iterative + Recursion

## 1. Iterative Approach

### Logic

- If `n <= 0` → `False`
- If `n == 1` → `True`
- Keep dividing `n` by `3`.
- Before dividing, check if `n` is divisible by `3`.
- If not divisible → `False`.
- If we reach `1` → `True`.

```python
class Solution:
    def isPowerOfThree(self, n):
        if n <= 0:
            return False

        if n == 1:
            return True

        while n > 1:
            if n % 3 != 0:
                return False

            n = n // 3

        return True
````

### Example

```text
27 → 9 → 3 → 1 → True

45 → 15 → 5 → not divisible by 3 → False
```

---

## 2. Recursive Approach

### Logic

* Same logic as the loop.
* Recursion replaces the `while` loop.
* Divide `n` by `3` and call the function again.
* `return` is important so the answer is passed back through all calls.

```python
class Solution:
    def isPowerOfThree(self, n):
        if n <= 0:
            return False

        if n == 1:
            return True

        if n % 3 != 0:
            return False

        return self.isPowerOfThree(n // 3)
```

### Example

```text
27
↓
9
↓
3
↓
1
↓
True
```

The `True` returns back through:

```text
isPowerOfThree(1) → True
isPowerOfThree(3) → True
isPowerOfThree(9) → True
isPowerOfThree(27) → True
```

## Main Difference

```text
Iterative → while loop repeatedly divides n

Recursive → function calls itself with n // 3
```

Both use the same basic idea:

```text
check → divide by 3 → repeat → reach 1
```
