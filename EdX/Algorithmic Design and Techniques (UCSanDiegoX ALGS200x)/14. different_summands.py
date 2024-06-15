# Start with the smallest number of candies (1) and keep adding the next smallest number until you can't add without exceeding n.
# If adding the next number would exceed n, give the remaining candies to the last child.

# Uses python3

import sys

def optimal_summands(n):
    summands = []
    k = 1
    while n > 0:
        if n - k > k:
            summands.append(k)
            n -= k
            k += 1
        else:
            summands.append(n)
            break
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')