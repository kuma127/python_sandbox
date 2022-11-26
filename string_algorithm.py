def is_anagram(s1: str, s2: str) -> bool:
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    return sorted(s1) == sorted(s2)

def is_palindrome(s1: str) -> bool:
    s = s1.lower()
    return s == s[::-1]

s1 = 'Emperor Octavian'
s2 = 'Captain over rome'
print(is_anagram(s1, s2))

s3 = 'Momo'
print(is_palindrome(s3))

s = 'Buy 1 get 2 free'
print([c for c in s if c.isdigit()][-1])

# challenge
str_list = ['selftaught', 'code', 'sit', 'eat', 'programming', 'dinner', 'one', 'two', 'coding', 'a', 'tech']
print([c for c in str_list if len(c) > 3])