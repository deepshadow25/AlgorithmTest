from math import gcd
lcm = lambda a, b:a*b/gcd(a, b)
solution = lambda n, m:[gcd(n,m), lcm(n, m)]