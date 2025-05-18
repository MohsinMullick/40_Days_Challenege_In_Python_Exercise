"""
2. Reverse String with Loop (Medium, Important)
a. Description: Reverse a string s using a while loop without slicing.
b. Example: Input: s = "hello" → Output: "olleh"
c. Relevance: Common interview question; tests loop control.
"""
s = "hello"
reverse_s =""
char=len(s)-1
while char >= 0:
    reverse_s += s[char]
    char -= 1
print(reverse_s)
####for loop reverse
s = "hello"
reverse_s = ""
for char in s:
    reverse_s = char + reverse_s
print(reverse_s)