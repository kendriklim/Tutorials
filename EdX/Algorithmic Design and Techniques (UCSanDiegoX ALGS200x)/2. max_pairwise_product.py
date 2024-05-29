# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0

def max_prod_fast(a):
    p1 = max(a)
    a.remove(p1)
    p2 = max(a)
    return p1*p2

result = max_prod_fast(a)
print(result)