def gcd(a,b):
    assert int(a) == a and int(b) == b, "Only postitive numbers"

    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

if __name__ == "__main__":
    import timeit
    a = int(input("Enter a : "))
    b = int(input("Enter b: "))
    print(timeit.timeit("gcd(a, b)", globals=globals()), gcd(a, b))