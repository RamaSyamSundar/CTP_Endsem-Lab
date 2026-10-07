def knapsack(n, max_capacity, weights, values):
    # Construct DP Table
    dp = [[0 for _ in range(max_capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, max_capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # Display DP Table
    print("\nDP Table:")
    for row in dp:
        print("\t".join(map(str, row)))

    # Display Maximum Achievable Value
    print(f"\nMaximum Achievable Value: {dp[n][max_capacity]}")

    # Identify Selected Products
    w = max_capacity
    selected_products = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_products.append(i)
            w -= weights[i - 1]

    selected_products.reverse()
    print("Selected Products (1-indexed):", *selected_products)


def main():
    n = int(input("Enter the number of products: "))

    weights = []
    values = []

    print("Enter weight and value for each product:")
    for i in range(n):
        w, v = map(
            int,
            input(f"Product {i + 1} (Weight Value): ").strip().split(),
        )
        weights.append(w)
        values.append(v)

    max_capacity = int(input("Enter maximum capacity/budget: "))

    knapsack(n, max_capacity, weights, values)


if __name__ == "__main__":
    main()
