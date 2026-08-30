# LeetCode 125 — Valid Palindrome

## Concept

**Two Pointers**

Use two pointers:

* `left` → starts from the beginning
* `right` → starts from the end
* Compare characters while moving both pointers toward the center.

## Approach

1. Initialize:

   * `left = 0`
   * `right = len(s) - 1`

2. Run while:

   ```python
   while left < right:
   ```

   We only need to compare pairs. When `left == right`, we are at the middle and don't need to compare it.

3. Ignore non-alphanumeric characters:

   ```python
   if not s[left].isalnum():
       left += 1
       continue
   ```

   ```python
   if not s[right].isalnum():
       right -= 1
       continue
   ```

   `.isalnum()` checks whether a character is a letter or number.

   `continue` skips the rest of the current iteration and starts the loop again.

4. Compare characters without considering uppercase/lowercase:

   ```python
   if s[left].lower() != s[right].lower():
       return False
   ```

5. If they match, move both pointers inward:

   ```python
   left += 1
   right -= 1
   ```

6. If every pair matches, return:

   ```python
   return True
   ```

## Key Pattern

```text
Skip invalid characters
        ↓
Compare left & right
        ↓
Different → False
Same → move both inward
        ↓
Repeat
        ↓
Finished → True
```

## Important Functions

* `isalnum()` → checks if character is a letter or number
* `lower()` → converts character to lowercase
* `continue` → skips current loop iteration

## Complexity

* **Time:** O(n)
* **Space:** O(1)

We only use two pointer variables and don't create another string.


## Approach 2 — Recursion

### Concept

**Recursion + Two Pointers**

Use `left` and `right` pointers and recursively check characters from the outside toward the center.

### Approach

1. Start with:

   ```python
   left = 0
   right = len(s) - 1
   ```

2. Create a recursive helper function:

   ```python
   helper(left, right)
   ```

3. **Base Case:**

   ```python
   if left >= right:
       return True
   ```

   If the pointers meet or cross, all required pairs have matched, so the string is a palindrome.

4. **Skip non-alphanumeric characters:**

   ```python
   if not s[left].isalnum():
       return helper(left + 1, right)
   ```

   ```python
   if not s[right].isalnum():
       return helper(left, right - 1)
   ```

   `isalnum()` checks whether a character is a letter or number.

5. **Compare characters:**

   ```python
   if s[left].lower() != s[right].lower():
       return False
   ```

   `.lower()` makes the comparison case-insensitive.

6. If the characters match, recursively move both pointers inward:

   ```python
   return helper(left + 1, right - 1)
   ```

7. Start recursion:

   ```python
   return helper(0, len(s) - 1)
   ```

### Recursion Flow

```text
Check left & right
       ↓
Invalid character?
   ↓           ↓
  Yes          No
   ↓            ↓
Skip it      Compare
              ↓
         Different?
          ↓       ↓
        Yes       No
         ↓         ↓
      False    Move inward
                   ↓
              Recursive call
                   ↓
             Repeat until
             left >= right
                   ↓
                 True
```

### Key Points

* `helper(left, right)` replaces the `while` loop.
* `left + 1` moves from left → right.
* `right - 1` moves from right → left.
* `left >= right` → base case → `True`.
* Any mismatch → `False`.
* `continue` is not needed because recursion immediately calls the helper again.

### Complexity

* **Time:** O(n)
* **Space:** O(n) — due to recursive call stack.
