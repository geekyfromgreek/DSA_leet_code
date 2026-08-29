
# Number of Steps — Recursion Notes

## Logic

- Reduce `num` until it becomes `0`.
- If `num` is **even** → divide by `2`.
- If `num` is **odd** → subtract `1`.
- Every operation is **1 step**, so add `1` to the recursive result.

## Base Case

```text
num == 0 → return 0
````

No more steps are needed.

## Recursive Calls

### Even

```python
return 1 + self.numberOfSteps(num // 2)
```

* `// 2` performs the current step.
* Recursive call calculates the remaining steps.
* `1 +` counts the current step.

### Odd

```python
return 1 + self.numberOfSteps(num - 1)
```

* `num - 1` performs the current step.
* Recursive call calculates the remaining steps.
* `1 +` counts the current step.

## Example: 14

```text
14 → 7 → 6 → 3 → 2 → 1 → 0
```

Going down → reduce `num`.

Coming back → count steps:

```text
0
↓
1
↓
2
↓
3
↓
4
↓
5
↓
6
```

## Important Recursion Idea

The recursive call returns a value to the **previous waiting call**.

```text
numberOfSteps(2) → 2
        ↓
numberOfSteps(3)
→ 1 + 2
→ 3
```

So:

> **Go down to the base case → return the answer → each previous call adds `1`.**

```
````md
# Number of Steps — Recursion Notes

## Logic

- Reduce `num` until it becomes `0`.
- If `num` is **even** → divide by `2`.
- If `num` is **odd** → subtract `1`.
- Every operation is **1 step**, so add `1` to the recursive result.

## Base Case

```text
num == 0 → return 0
````

No more steps are needed.

## Recursive Calls

### Even

```python
return 1 + self.numberOfSteps(num // 2)
```

* `// 2` performs the current step.
* Recursive call calculates the remaining steps.
* `1 +` counts the current step.

### Odd

```python
return 1 + self.numberOfSteps(num - 1)
```

* `num - 1` performs the current step.
* Recursive call calculates the remaining steps.
* `1 +` counts the current step.

## Example: 14

```text
14 → 7 → 6 → 3 → 2 → 1 → 0
```

Going down → reduce `num`.

Coming back → count steps:

```text
0
↓
1
↓
2
↓
3
↓
4
↓
5
↓
6
```

## Important Recursion Idea

The recursive call returns a value to the **previous waiting call**.

```text
numberOfSteps(2) → 2
        ↓
numberOfSteps(3)
→ 1 + 2
→ 3
```

So:

> **Go down to the base case → return the answer → each previous call adds `1`.**

```
```
