# Complexity O(n), Finding Fibonacci# numbers, using dynamic programming

def dynamicFibonacci(n, d):
    if n in d:
        return d[n]
    else:
        d[n] = dynamicFibonacci(n-1, d) + dynamicFibonacci(n-2, d)
        return d[n]

print(dynamicFibonacci(6, {1: 1, 2: 2}))