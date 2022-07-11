def power_of_n(base, exp):
    assert exp >= 0, "Only postive integers for exponent"

    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * power_of_n(base, exp - 1)


if __name__ == "__main__":
    import timeit
    base = int(input("Enter a base: "))
    exp = int(input("Enter the exponent: "))
    print(timeit.timeit("power_of_n(base, exp)", globals=globals()), power_of_n(base, exp))