# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))

# Revised
import sys

def fibonacci_sum_fast(n):
    if n <= 1:
        return n

    pisano_period = 60
    n = n % pisano_period

    if n == 0:
        return 0
    elif n == 1:
        return 1

    previous, current = 0, 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10
        sum = (sum + current) % 10

    return sum

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_fast(n))
