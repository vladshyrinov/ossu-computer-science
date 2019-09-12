# log2N - algorithm coplexity
# Finding the root of a number with a binary-search

def root(num, root, epsilon):
    if root % 2 == 0 and num < 0:
        print(f'The paired root {root} of a negative number {num} is not considered')
        return 
    low = 0
    if num > 0 and num < 1:
        high = 1
    elif num < 0 and num > -1:
        high = -1
    else:
        high = num
    guess = (high - low) / 2
    checkNum = guess**root

    while abs(checkNum - num) >= epsilon: 
        if abs(checkNum) > abs(num):
            high = guess
        else:
            low = guess
        guess = (high - low) / 2 + low
        checkNum = guess**root
        if checkNum == num:
            print(f"The root {root} of {num} is {guess}")
        elif abs(checkNum - num) < epsilon:
            print(f"The root {root} of {num} is close to {guess}; epsilon: {epsilon}")

root(625, 4, 0.01)
root(-625, 4, 0.1)
root(-125, 3, 0.1)
root(1, 3, 0.0001)
root(0.1, 2, 0.1)
root(-0.3, 3, 0.01)