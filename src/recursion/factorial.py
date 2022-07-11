def factorial(n):
    assert n >=0 and int(n) == n, 'The number must be postitive integer only'
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    import timeit
    number = int(input("Enter a number: "))
    print(timeit.timeit("factorial(number)", globals=globals()), factorial(number))