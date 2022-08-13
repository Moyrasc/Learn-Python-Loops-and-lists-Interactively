arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:

def is_odd(number):
    if number % 2 == 0:
        return False
    else:
        return True

def sumOdds(items):
    total = 0

    for i in items:
        if is_odd(i):
            total += i
    
    return total

print(sumOdds(arr))
