#!/usr/bin/python3
"""FizzBuzz implementation"""

def fizzbuzz(n):
    """
    Print numbers from 1 to n, but:
    - print "Fizz" if divisible by 3
    - print "Buzz" if divisible by 5
    - print "FizzBuzz" if divisible by both 3 and 5
    """
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return " ".join(result)

if __name__ == "__main__":
    import sys
    if len(sys.argv) <= 1:
        print("Usage: ./0-fizzbuzz.py <number>")
        sys.exit(1)
    
    number = int(sys.argv[1])
    print(fizzbuzz(number))
