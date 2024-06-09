# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))



# Revised
import sys

def fibonacci_partial_sum_optimized(from_, to):
    if to < from_:
        return 0

    # Pisano period for % 10 is 60
    pisano_period = 60

    # Precompute all Fibonacci numbers % 10 up to one Pisano period
    fib_mods = [0, 1]
    for i in range(2, pisano_period):
        fib_mods.append((fib_mods[i-1] + fib_mods[i-2]) % 10)

    # Sum the Fibonacci numbers from 'from_' to 'to' using the precomputed values
    sum = 0
    for i in range(from_ % pisano_period, to % pisano_period + 1):
        sum += fib_mods[i]

    return sum % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_optimized(from_, to))