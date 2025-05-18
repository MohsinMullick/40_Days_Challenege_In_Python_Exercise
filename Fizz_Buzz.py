"""
4. FizzBuzz (Easy, Important)
a. Description: For numbers 1 to n, return "Fizz" for multiples of 3,
"Buzz" for
multiples of 5, "FizzBuzz" for both, using a for loop.
b. Example: Input: n = 5 → Output: [1,2,"Fizz",4,"Buzz"]
c. Relevance: Classic interview problem; tests loop and conditionals.
"""
def fizzbuzz(n):
    result = []
    for num in range(1, n+1):
        if num % 3 == 0 and num % 5 == 0:
            result.append("FizzBuzz")
        elif num % 3 == 0:
            result.append("Fizz")
        elif num % 5 == 0:
            result.append("Buzz")
        else:
            result.append(num)
    return result
print(fizzbuzz(5))

