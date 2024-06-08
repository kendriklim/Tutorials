# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))


# Revised
import sys

def pisano_period(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m
        # This condition is checked to find the period
        if (previous == 0 and current == 1):
            return i + 1

def get_fibonacci_huge(n, m):
    if n <= 1:
        return n

    # Get the period
    period = pisano_period(m)

    # Reduce n modulo the period
    n = n % period

    if n == 0:
        return 0
    elif n == 1:
        return 1

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))