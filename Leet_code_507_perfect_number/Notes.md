# LeetCode 507 — Perfect Number

For the problem, we had to check whether a number is a **perfect number**.

A perfect number is a number where the sum of its **proper divisors** is equal to the number itself.

Example:

28 → 1 + 2 + 4 + 7 + 14 = 28

So `28` is a perfect number.

## Approach 1 — Handle 1 at the End

- Used a `for` loop only up to `√num`.
- Used `%` to check if `i` is a divisor.
- Used `num // i` to find the **paired divisor**.
- Added `i` and its paired divisor to `sum`.
- Used `num // i != i` to avoid counting the same divisor twice for perfect squares.
- Used `num // i != num` to avoid adding `num` itself.
- After calculating the sum, checked `sum == num`.
- If `num == 1`, returned `False` because `1` is not a perfect number.

### Logic

```text
Find divisors
↓
Find paired divisors
↓
Don't count duplicate divisor
↓
Don't count num itself
↓
Check sum == num
↓
Handle num = 1
````

## Approach 2 — Handle 1 First

Instead of checking `num == 1` after calculating the divisor sum, we can handle it at the beginning:

```text
if num == 1:
    return False
```

Then the rest of the logic becomes simpler because `1` is already handled.

### Logic

```text
Check if num == 1
↓
If yes → False
↓
Find divisors up to √num
↓
Find paired divisors
↓
Add proper divisors
↓
Check sum == num
```

## Paired Divisor

If `i` is a divisor:

```text
i × (num // i) = num
```

Example for `28`:

```text
1 × 28
2 × 14
4 × 7
```

`2` and `14` are paired divisors.

## Why √num?

Factors always come in pairs.

Once we reach `√num`, the remaining factors have already been found as paired divisors, so we don't need to check all the way to `num`.

Example:

```text
36

1 × 36
2 × 18
3 × 12
4 × 9
6 × 6
```

After `6 = √36`, the remaining factors are already found.

## Important Conditions

```python
num % i == 0
```

Checks whether `i` is a divisor.

```python
num // i
```

Finds the paired divisor.

```python
num // i != i
```

Prevents counting the same divisor twice for perfect squares.

```python
num // i != num
```

Prevents adding `num` itself.

## Edge Case — 1

`1` is not a perfect number because its only divisor is itself.

```text
Proper divisors of 1 = none
Sum = 0
```

So:

```text
1 → False
```

Handling `1` **before the loop** is cleaner than checking it after calculating the sum.

## Complexity

* **Time:** O(√n) because we only check up to the square root.
* **Space:** O(1) because we don't store the divisors.