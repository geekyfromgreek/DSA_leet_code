# LeetCode 242 — Valid Anagram

## Concept

**Hash Map / Dictionary + Frequency Counting**

The goal is to check whether two strings contain the **same characters with the same frequency**, regardless of their order.

Example:

```text
s = "anagram"
t = "nagaram"

→ True
```

---

## Approach

### 1. Check lengths

```python
if len(s) != len(t):
    return False
```

Two anagrams must have the same number of characters.

---

### 2. Create a dictionary

```python
count = {}
```

The dictionary stores:

```text
character → frequency
```

---

### 3. Count characters in `s`

```python
for char in s:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
```

Example:

```text
s = "aabbc"

count = {
    'a': 2,
    'b': 2,
    'c': 1
}
```

---

### 4. Subtract characters using `t`

```python
for char in t:
    if char not in count:
        return False

    count[char] -= 1
```

For every character in `t`, reduce its frequency.

If a character doesn't exist in `s`:

```python
if char not in count:
    return False
```

The strings cannot be anagrams.

---

### 5. Check for too many occurrences

```python
if count[char] < 0:
    return False
```

If the count becomes negative, `t` contains that character **more times than `s`**.

Example:

```text
s = "aab"
t = "aaa"

count['a']:

2 → 1 → 0 → -1
             ↑
          Too many
```

So return `False`.

---

### 6. If everything passes

```python
return True
```

Because:

* Both strings have the same length
* Every character in `t` exists in `s`
* No character is used more times than available

Therefore, they are anagrams.

---

## Key Idea

```text
Count characters in s
        ↓
Subtract characters from t
        ↓
Missing character? → False
Count becomes negative? → False
        ↓
Everything matches
        ↓
True
```

---

## Example

```text
s = "anagram"
t = "nagaram"
```

Count `s`:

```text
a → 3
n → 1
g → 1
r → 1
m → 1
```

Process `t`:

```text
n → 0
a → 2
g → 0
a → 1
r → 0
a → 0
m → 0
```

Everything balances → `True`.

---

## Complexity

* **Time:** O(n) — traverse both strings once
* **Space:** O(k) — dictionary stores distinct characters

Where `k` is the number of unique characters.

---

## Pattern Learned

**Frequency Counting**

Use a dictionary when a problem asks you to:

* Count occurrences
* Compare character frequencies
* Find duplicates
* Check whether two collections contain the same elements/frequencies

### Important Dictionary Pattern

```python
if key in count:
    count[key] += 1
else:
    count[key] = 1
```

This is the basic manual way to build a frequency map.
