# Fibonacci — Recursion Notes

## Logic

- `fib(n)` needs the previous **2 Fibonacci numbers**.
- So we recursively calculate:
  - `fib(n-1)`
  - `fib(n-2)`
- Add both results to get `fib(n)`.

## Base Case

```text
n <= 1

fib(0) = 0

fib(1) = 1

Stop recursion and return n.


Recursion Flow

fib(n)
 ↓
fib(n-1) + fib(n-2)
 ↓
keep breaking down
 ↓
reach n = 0 or 1
 ↓
return values
 ↓
add them while coming back

Problem with Basic Recursion

The same values are calculated again and again.

Example:

fib(5)
├── fib(3)
└── fib(4)
    ├── fib(2)  ← repeated
    └── fib(3)  ← repeated

So runtime becomes very high.

Time:  O(2^n)
Space: O(n)

Next concept: Memoization — save already calculated results instead of calculating them again.