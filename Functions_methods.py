
def isprime(n):
    if (n <= 1):
        return False
    for x in range(2, n):
        if n % x == 0:
            return False

    else:
        return True
    

n = 10
if isprime(n):
    print( 'Is prime {}' .format(n))
else:
    print('is not a prime {}'.format(n))