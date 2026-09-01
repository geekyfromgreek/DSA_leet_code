# LeetCode 121 — Best Time to Buy and Sell Stock

## Concept

**Array Traversal + Tracking Minimum and Maximum**

The goal is to find the maximum profit by:

* Buying at a low price
* Selling at a later higher price

## Approach

1. Start with the first price as the minimum:

   ```python
   min_price = prices[0]
   ```

2. Start maximum profit at `0`:

   ```python
   max_profit = 0
   ```

3. Traverse every price:

   ```python
   for price in prices:
   ```

4. If the current price is lower than the minimum seen so far, update it:

   ```python
   if price < min_price:
       min_price = price
   ```

5. Calculate the profit if we sell at the current price:

   ```python
   profit = price - min_price
   ```

6. Keep the largest profit:

   ```python
   if profit > max_profit:
       max_profit = profit
   ```

7. Return the maximum profit:

   ```python
   return max_profit
   ```

## Example

```text
prices = [7, 1, 5, 3, 6, 4]

minimum price → 1
best selling price → 6

profit = 6 - 1 = 5
```

Answer:

```text
5
```

## Key Idea

Don't compare every possible buy/sell combination.

While moving through the array, simply remember:

```text
minimum price seen so far
            ↓
calculate current profit
            ↓
maximum profit seen so far
```

## Important

The stock must be **bought before it is sold**.

That's why we traverse from left to right and only use the minimum price seen **before/currently**.

## Complexity

* **Time:** O(n) — visit each price once
* **Space:** O(1) — only use a few variables

## Pattern Learned

**Track a running minimum/maximum while traversing an array.**

This pattern is useful for many array problems where you need to find the best value while scanning the elements once.
