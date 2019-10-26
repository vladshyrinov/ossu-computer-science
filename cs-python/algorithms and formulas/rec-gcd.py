# Finding the greates common divisor recursively

def recGcd(a, b):
    if b == 0:
        return a
    else:
        return recGcd(b, a % b)

print(recGcd(10, 5))
