# Define a recursive procedure is_palindrome, that takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.

# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?

def is_palindrome(s):
    if s=='':
        return True
    s=s.lower()
    i=0
    j=-1
    while i < len(s):
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True


def is_palindrome(s):
    if s == '':
        return True
    s=s.lower()
    for i, j in zip(s, reversed(s)):
        if i!=j:
            return False
    return True


def is_palindrome(s):
    if s == '':
        return True
    s=s.lower()
    reverse_s=reversed(s)
    if list(s)!=list(reverse_s):
        return False
    return True

def is_palindrome(s):
    if s == '':
        return True
    s=s.lower()
    j=''
    j=j.join(reversed(s))
    if s!=j:
        return False
    return True

def is_palindrome(s):
    if s == '':
        return True
    s=s.lower()
    if s!=s[::-1]:
        return False
    return True

def is_palindrome(s):
    if s == '':
        return True
    s=s.lower()
    i=0
    j=-1
    while i < len(s):
        if s[i]!=s[j]:
            return False
        else:
            i+=1
            j-=1

    return True

def is_palindrome(s):
    if len(s) < 2:
        return True
    s=s.lower()
    if s[0]!=s[-1]:
        return False
    else:
        is_palindrome(s[1:-1])
    return True

print(is_palindrome(''))
# >>> True
print(is_palindrome('abab'))
# >>> False
print(is_palindrome('abba'))
# >>> True
print(is_palindrome('kayaK'))
# >>> True