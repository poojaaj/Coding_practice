def palindrome(s):
    s = ''.join(e for e in s if e.isalnum())
    print(s)


s = "A man, a plan, a canal: Panama"
palindrome(s)