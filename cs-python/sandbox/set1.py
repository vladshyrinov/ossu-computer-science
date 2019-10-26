def vowelcCounter(s):
    '''
    Argument s: String
    Prints number of vowels in the string 
    '''
    vowels = "aeiou"

    count = 0    
    for l in s:
        if l in vowels:
            count += 1
    print("Number of vowels", str(count))

vowelcCounter("hello")

def bobCounter(s):
    '''
    Argument s: String
    Prints number of bob substring in the string 
    '''   
    curStr = ""
    count = 0
    for l in s:
        if l == "b":
            if len(curStr) == 0:
                curStr += l
            elif len(curStr) == 2:
                count += 1
                curStr = l
        elif l == "o" and len(curStr) == 1:
            curStr += l
        else:
            curStr = ""
    print("Number of times bob occurs is:", str(count))

bobCounter("kboobbobbrbobbboedbobbbobpobobb")

def longestSubstring(s):
    '''
    Argument s: String
    Prints the longest substring in the alphabetical order in the string 
    '''
    longestSubstr = ""
    currentStr = ""
    lastCode = 0
    for l in s:
        codeDiff = ord(l) - lastCode
        if codeDiff >= 0:  
            currentStr += l
        else:
            if len(currentStr) > len(longestSubstr):
                longestSubstr = currentStr
            currentStr = l
        lastCode = ord(l)
    if len(currentStr) > len(longestSubstr):
        longestSubstr = currentStr
            

    print("Longest substring in alphabetical order is:", longestSubstr)

longestSubstring("xvnupdjjm")

        
    
