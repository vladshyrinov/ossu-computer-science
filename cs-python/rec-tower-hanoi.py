# Solving the Hanoi tower problem recursively

moves = 0

def towerHanoi(n, fr, to, spare):
    global moves
    if n == 1:
        moves += 1
        print(f"Move from spike {fr} to spike {to}")
    else:
        towerHanoi(n-1, fr, spare, to)
        towerHanoi(1, fr, to, spare)
        towerHanoi(n-1, spare, to, fr)

towerHanoi(4, "1", "2", "3")
print(f'Needed quantity of moves: {moves}')