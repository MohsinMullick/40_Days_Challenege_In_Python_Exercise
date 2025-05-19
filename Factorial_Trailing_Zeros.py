"""
10.Factorial Trailing Zeroes (Medium)
a. Description: Find the number of trailing zeroes in n!
 using a while loop.
b. Example: Input: n = 5 → Output: 1 (5! = 120)
c. Relevance: Tests mathematical loop logic.
"""
def trailing_zeroes(n):
    count = 0
    # Count how many times 5 is a factor in 1..n
    while n > 0:
        n = n // 5
        count += n
    return count
n = 5
print(trailing_zeroes(n))