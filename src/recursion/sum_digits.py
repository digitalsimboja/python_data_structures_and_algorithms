def sum_of_digits(n):
    assert n >= 0 and int(n) == n, "Enter postive integers only"
    
    if n == 0:
        return 0
    else:
        return int(n % 10) + sum_of_digits(int(n / 10))


if __name__ == "__main__":
    import timeit
    number = int(input("Enter a number: "))
    print(timeit.timeit("sum_of_digits(number)", globals=globals()), sum_of_digits(number))