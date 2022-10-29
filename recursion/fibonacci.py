def fib(n):
    assert n >= 0 and int(n) == n, "Only postive numbers allowed"
    if n in [0, 1]: return n
    else:
        return fib(n-1) + fib(n-2)

def fib_fast(n):
    fibonacci_list = [0,1]
    for i in range(2, n + 1):
        new_fibonacci_list = fibonacci_list[i - 1] + fibonacci_list[i - 2]
        fibonacci_list.append(new_fibonacci_list)

    return fibonacci_list[-1]

def fib_fast2(n):
    if n < 1:
        return n
    
    a,b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    import timeit
    number = int(input("Enter a number: "))
    print(timeit.timeit("fib(number)", globals=globals()), fib(number))
    print(timeit.timeit("fib_fast(number)", globals=globals()), fib_fast(number))
    print(timeit.timeit("fib_fast2(number)", globals=globals()), fib_fast2(number))