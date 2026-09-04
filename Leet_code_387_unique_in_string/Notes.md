# LeetCode 387 — First Unique Character in a String

## Concept

**Hash Map / Dictionary + Frequency Counting**

The goal is to find the **index of the first character that appears only once** in a string.

Example:

```text
s = "leetcode"

l → 1
e → 3
t → 1
c → 1
o → 1
d → 1

Answer → 0
```

`l` appears only once and is the first unique character.

---

## Approach

### 1. Create a dictionary

```python
count = {}
```

The dictionary stores:

```text
character → frequency
```

---

### 2. First pass — count every character

```python
for i in range(len(s)):
    if s[i] in count:
        count[s[i]] = count[s[i]] + 1
    else:
        count[s[i]] = 1
```

For:

```text
"leetcode"
```

the dictionary becomes:

```text
{
    'l': 1,
    'e': 3,
    't': 1,
    'c': 1,
    'o': 1,
    'd': 1
}
```

### Important

* `i` → index
* `s[i]` → character at that index
* `count[s[i]]` → frequency of that character

---

### 3. Second pass — find the first unique character

```python
for i in range(len(s)):
    if count[s[i]] == 1:
        return i
```

Go through the string **from left to right**.

The first character whose frequency is `1` is the answer.

Return `i` because the problem asks for the **index**, not the character.

---

### 4. If no unique character exists

```python
return -1
```

If every character appears more than once, return `-1`.

---

## Key Idea

```text
First pass
    ↓
Count character frequencies
    ↓
Second pass
    ↓
Find first character with count == 1
    ↓
Return its index
```

### Example

```text
s = "loveleetcode"

index:  0 1 2 3 4 5 6 7 8 9 10 11
char:   l o v e l e e t c o  d  e
```

Frequency:

```text
l → 2
o → 2
v → 1  ← first unique
e → 4
...
```

Therefore:

```text
return 2
```

---

## Complexity

* **Time:** O(n) — two passes through the string
* **Space:** O(k) — dictionary stores the distinct characters

Where `k` = number of unique characters.

---

## Pattern Learned

**Frequency Counting + Two-Pass Traversal**

This pattern is useful when you need to:

* Count occurrences
* Find unique characters
* Find duplicates
* Compare frequencies
* Find the first/last element satisfying a frequency condition

### Dictionary Pattern

```python
if key in count:
    count[key] += 1
else:
    count[key] = 1
```
