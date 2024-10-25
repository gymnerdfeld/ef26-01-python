def fact_mit_for_loop(n):
    res = 1
    for i in range(n):
        res = res * (i + 1)
    return res


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

print(fact(4))

assert fact(0) == 1
assert fact(1) == 1
assert fact(2) == 2
assert fact(5) == 120
