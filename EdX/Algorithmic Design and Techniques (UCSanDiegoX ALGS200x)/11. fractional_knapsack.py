# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # Calculate value-to-weight ratio for each item
    value_weight_ratio = [(v / w, w) for v, w in zip(values, weights)]
    # Sort items by value-to-weight ratio in decending order
    value_weight_ratio.sort(reverse=True, key=lambda x: x[0])

    for ratio, weight in value_weight_ratio:
        if capacity == 0:
            return value
        # Take as much as possible of the highest value-to-weight ratio item
        amount = min(weight, capacity)
        value += amount * ratio
        capacity -= amount
    
    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))