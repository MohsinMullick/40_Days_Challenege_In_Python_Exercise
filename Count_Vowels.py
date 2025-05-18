"""
5. Count Vowels (Easy)
a. Description: Count vowels in a string s using a for loop.
b. Example: Input: s = "hello" → Output: 2 (e, o)
c. Relevance: Tests string iteration.
"""
s="hello"
check_vowels="aeiou"
count=0
for vowels in str(s):
    if vowels in check_vowels:
        count+=1
print(count)