def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


def tailFibonacci(n, before1=1, before2=0):
    if n == 0:
        return before2
    if n == 1:
        return before1

    return tailFibonacci(n-1, before1 + before2, before1)


# def fibo(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1

#     bef1 = 1
#     bef2 = 0

#     for i in range(n):
#         bef1, bef2 = bef1 + bef2, bef1

#     return bef2
