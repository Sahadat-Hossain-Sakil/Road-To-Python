s = input("Enter a string for test : ")
if s == s[len(s)::-1] :
    print(s, "is a palindrome word")
else :
    print(s, "is not a palindrome word")