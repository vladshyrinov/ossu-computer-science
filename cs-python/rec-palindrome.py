# The function is checking recursively if the phrase is a palindrome or not

def isPalindrome(s):
    def getJustLettersFromString(s):
        s = s.lower()
        formatedStr = ''
        for c in s:
            if ord(c) > 96 and ord(c) < 123:
                formatedStr += c
        return formatedStr
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(getJustLettersFromString(s))

print(isPalindrome('Eva, can I see bees in a cave?'))
print(isPalindrome('Sorry, Sam'))