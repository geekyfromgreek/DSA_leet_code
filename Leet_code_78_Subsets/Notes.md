
# Subsets — Recursion Notes

## Theory

- **TAKE** → include `nums[i]` in the current subset.
- **DON'T TAKE** → skip `nums[i]` and move to the next index.
- For every element, we try **both TAKE and DON'T TAKE**.
- **`i`** → current index we are deciding.
- **`current`** → temporary subset we are building.
- **`result`** → stores all completed subsets.
- **`helper()`** → recursive function that handles the TAKE / DON'T TAKE decisions.
- **`append()`** → TAKE the element.
- **`pop()`** → undo the TAKE so we can try DON'T TAKE.
- **`copy()`** → saves a snapshot of `current` because `current` keeps changing.
- **Base case** → `i >= len(nums)` means no elements are left to decide.
- **`return`** → finishes the current recursive call and goes back to the call that created it.

## Recursion Steps

For every element:

1. TAKE → `append(nums[i])`
2. Recurse → move to `i + 1`
3. Return after finishing that branch
4. `pop()` → undo the TAKE
5. DON'T TAKE → recurse with `i + 1`
6. Repeat for the next element
7. When `i >= len(nums)` → save `current.copy()` in `result`

### Example: `[1,2,3]`

```text
1 → TAKE / DON'T TAKE
2 → TAKE / DON'T TAKE
3 → TAKE / DON'T TAKE
````

This gives all possible subsets:

```text
[1,2,3]
[1,2]
[1,3]
[1]
[2,3]
[2]
[3]
[]
```

```
```
