"""
6. Count Primes (Easy)
a. Description: Count prime numbers less than n using a for loop and helper
function.
b. Example: Input: n = 10 → Output: 4 (2,3,5,7)
c. Relevance: Introduces nested loops for primality testing.
"""
def is_prime(num):
    """This function checks whether a given number (num) is a prime number"""
    if num < 2:
        # If the number is less than 2, immediately return False
        # because 0 and 1 are not prime numbers
        # Prime numbers must be greater than 1
        return False
    for i in range(2, int(num**0.5) + 1):
        """
        This loop runs from 2 up to the square root of the number
        Why square root? Because if a number has a factor larger than 
        its square root, it must also have a corresponding factor smaller 
        than the square root
        """
        if num % i == 0:
            return False
    return True  # This should be outside the for loop
def count_primes(n):
    """Count the number of primes less than n."""
    count = 0
    primes=()
    for num in range(2, n):
        if is_prime(num):
            primes+= (num,)
            count+=1
    return primes,count
n = int(input("n = "))
prime_numbers, total_primes = count_primes(n)
# Unpack both return values at once
print(total_primes)
print(prime_numbers)











