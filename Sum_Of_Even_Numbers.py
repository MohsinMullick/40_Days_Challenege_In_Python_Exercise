"""
1. Sum of Even Numbers (Easy)
a. Description: Compute the sum of even numbers in a list
 nums using a for
loop.
b. Example: Input: nums = [1,2,3,4] → Output: 6
c. Relevance: Tests basic for loop and conditionals.
"""
nums=[1,2,3,4]
sum=0
for i in nums:
    if int(i)%2==0:
        sum+=i
print(sum)


