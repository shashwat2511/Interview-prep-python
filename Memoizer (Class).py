# Testing Code: Fibonacci Function
# Same as shown in video
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# Testing Code: Binomial Coefficient Function
# Same as shown in video
def nCr(n, r):
    if r == 0 or r == n:
        return 1
    else:
        return nCr(n - 1, r - 1) + nCr(n - 1, r)


# Memoizer class
class Memoizer:
    # Entry point for Memoization capability: Class function memoize()
    # Parameters: The function you want to memoize
    # Returns: A tuple containing:
    #    (1) The memoized function (replace your original function with it)
    #    (2) An object of the Memoizer class for the function you have memoized
    def memoize(f):
        memoObj = Memoizer()

        def f_memo(*params):
            memoObj.count += 1
            key = str(params)

            if key in memoObj.memo:
                return memoObj.memo[key]
            else:
                ans = f(*params)
                memoObj.memo[key] = ans
                return ans

        return f_memo, memoObj

    def __init__(self):
        self.memo = {}  # Memo Table dictionary
        self.count = 0  # Counter for number of steps

    def reset(self):
        self.memo = {}
        self.count = 0


fib, fibMemo = Memoizer.memoize(fib)
print(f"Answer of fib(30): {fib(30)}")
print(f"Memo Table: {fibMemo.memo}")
print(f"Number of steps: {fibMemo.count}")

print()

nCr, ncrMemo = Memoizer.memoize(nCr)
print(f"Answer of nCr(20,8): {nCr(20,8)}")
print(f"Number of steps: {ncrMemo.count}")