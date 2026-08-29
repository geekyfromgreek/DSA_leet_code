Ah, yes — you mean you also did the **Python slicing approach**:

```python
s[:] = s[::-1]
```

Then your notes should be:

````md
# Reverse String — Two Approaches

## Approach 1: Recursion + Two Pointers

- `left = 0`
- `right = len(s) - 1`
- If `left >= right` → stop.
- Swap `s[left]` and `s[right]`.
- Move inward:
  - `left + 1`
  - `right - 1`
- Recursively repeat.

```text
helper(0,4)
→ swap
→ helper(1,3)
→ swap
→ helper(2,2)
→ stop
````

## Approach 2: Slicing

```python
s[:] = s[::-1]
```

* `s[::-1]` creates a reversed copy of the list.
* `s[:] =` puts that reversed content back into the original list.
* This keeps the **same list object**, which is important because LeetCode asks for an in-place modification.

Example:

```text
s = [h,e,l,l,o]

s[::-1]
→ [o,l,l,e,h]

s[:] = [o,l,l,e,h]
```

### Difference

```text
Recursion → manually reverses using swaps
Slicing   → Python directly creates the reversed sequence
```
