def sqr_power_mod(a, n, m):
    p = 1
    b = a
    k = n
    while k > 0:
        if k % 2 == 0:
            k //= 2
            b = b * b % m
        else:
            k -= 1
            p = p * b % m
    return p
