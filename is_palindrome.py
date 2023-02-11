def is_palindrome(s):
    s = s.lower()
    print(s)
    word = ''

    for i in reversed(range(len(s))):
        word += s[i]
         
    if (s == word):
        return True
    else:
        return False
