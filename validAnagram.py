def anagram(s,t):
    if len(s) != len(t):
        print("not a anagram")
    else:
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[i] != t[i]:
                print("not a anagram")
            else:
                print("anagram")


s = "rat"
t = "car"
anagram(s,t)