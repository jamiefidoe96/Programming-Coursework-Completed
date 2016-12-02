def is_prime(x):
    return check(x, x-1)

def check(n, k):
    # your conditional check
    if n%k == 0: #not a prime
        return False
    elif k == 2: #2 is the last number to be checked
        return True #it's a prime number if this is reached
    else: #we need to keep checking
        return check(n, k-1) #recursive call
