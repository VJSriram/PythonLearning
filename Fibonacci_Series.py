# Fibonacci series
# The sum of two numbers defines fibonacci 
from test.sortperf import flush

a, b = 0, 1
while b < 1000:
    print(b, end = ' ', flush = True)
    a, b = b, a + b
    
print() # line ending