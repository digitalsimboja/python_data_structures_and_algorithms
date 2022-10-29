def decimal_to_binary(n):
    assert int(n) == n, "The number must be integer only"

    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimal_to_binary(int(n / 2))


if __name__ == "__main__":
    import timeit
    n = int(input("Enter a number : "))
    print(timeit.timeit("decimal_to_binary(n)", globals=globals()), decimal_to_binary(n))