def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def nCr(n, r):
    if r == 0 or r == n:
        return 1
    else:
        return nCr(n - 1, r - 1) + nCr(n - 1, r)


numsteps = 0


def count(f):
    def f_count(*params):
        global numsteps
        numsteps += 1

        return f(*params)

    return f_count


memo = {}


def memoize(f):
    def f_memo(*params):
        global memo

        key = str(params)
        if key in memo:
            return memo[key]
        else:
            ans = f(*params)
            memo[key] = ans
            return ans

    return f_memo


# fib = memoize(fib)
# fib = count(fib)
# print(fib(30))
# print(numsteps)

nCr = memoize(nCr)
nCr = count(nCr)
print(nCr(20, 9))
print(numsteps)
print(memo)