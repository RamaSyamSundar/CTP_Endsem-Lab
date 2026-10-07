# 0/1 Knapsack Problem using Dynamic Programming

## Aim

To implement the **0/1 Knapsack Problem** using **Dynamic Programming** to determine the combination of products that maximizes the total value without exceeding the given capacity.

## Algorithm / Procedure

1. Read the total number of products `N`, weights, values, and maximum capacity `C`.
2. Create a 2D DP table `dp` of size `(N + 1) x (C + 1)`, initialized with zeros.
3. For each product and capacity:
   - If the product weight is less than or equal to the current capacity:
     - Calculate the maximum of:
       - Not selecting the product.
       - Selecting the product and adding its value to the best value for the remaining capacity.
   - Otherwise, copy the value from the previous row.
4. Trace back through the DP table to identify the selected products.
5. Display the DP table, maximum achievable value, and selected products.

## Recurrence Relation

If `weights[i-1] <= w`:

```text
dp[i][w] = max(
    dp[i-1][w],
    values[i-1] + dp[i-1][w - weights[i-1]]
)
```

Otherwise:

```text
dp[i][w] = dp[i-1][w]
```

## Time and Space Complexity

- **Time Complexity:** O(N × C)
- **Space Complexity:** O(N × C)

Where:
- `N` = number of products
- `C` = maximum capacity

## Program

The complete Python implementation is available in [knapsack_dp.py](knapsack_dp.py).

## How to Run

Make sure Python 3 is installed.

```bash
python knapsack_dp.py
```

## Sample Input

```text
Enter the number of products: 3
Enter weight and value for each product:
Product 1 (Weight Value): 2 3
Product 2 (Weight Value): 3 4
Product 3 (Weight Value): 4 5
Enter maximum capacity/budget: 5
```

## Sample Output

```text
DP Table:
0	0	0	0	0	0
0	0	3	3	3	3
0	0	3	4	4	7
0	0	3	4	5	7

Maximum Achievable Value: 7
Selected Products (1-indexed): 1 2
```

## Result

For the sample input, the maximum achievable value is **7**, obtained by selecting **Product 1 and Product 2** within the capacity of 5.
