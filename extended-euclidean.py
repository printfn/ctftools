#!/usr/bin/env python3

def ee(a, b):
    (old_r, r) = (a, b)
    (old_s, s) = (1, 0)
    (old_t, t) = (0, 1)

    while r != 0:
        quotient = old_r // r
        (old_r, r) = (r, old_r - quotient * r)
        (old_s, s) = (s, old_s - quotient * s)
        (old_t, t) = (t, old_t - quotient * t)

    print(f"bezout: {old_s}, {old_t}")
    print(f"gcd: {old_r}")
    print(f"quotients by gcd: {t}, {s}")

ee(26513, 32321)
