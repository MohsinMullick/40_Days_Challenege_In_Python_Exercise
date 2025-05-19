"""
9. Palindrome Check with Loop (Easy, Important)
a. Description: Check if a string s is a palindrome using a while loop, ignoring
non-alphanumeric characters.
b. Example: Input: s = "A man, a plan, a canal: Panama" → Output:
True
c. Relevance: Tests while loop with two pointers.
"""
def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        # Skip non-alphanumeric characters from left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric characters from right
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
# Test case
s = "A man, a plan, a canal: Panama"
print(is_palindrome(s))  # Output: True