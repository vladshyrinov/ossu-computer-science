# Finding the root with using of the Newton-Rathson theorem:
# The butter guess than the current one can be guess - (guess^power - y) / (guess^power - y)' [power * guess]

def newtonRaphsonSquareRoot(y):
    guess = y / 2
    epsilon = 0.01
    while abs(guess*guess - y) >= 0.01:
        print(guess)
        guess = guess - abs(guess*guess - y) / (2 * guess)
    return guess

print(newtonRaphsonSquareRoot(25))