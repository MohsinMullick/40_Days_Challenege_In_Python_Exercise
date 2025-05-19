"""
7. Longest Increasing Subsequence Length (Medium, Important)
a. Description: Find the length of the longest increasing subsequence in
nums
using nested for loops.
b. Example: Input: nums = [10,9,2,5,3,7,101,18] → Output: 4
c. Relevance: Tests loop-based dynamic programming; common in interviews.
"""
def length_of_lis(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(length_of_lis(nums))
