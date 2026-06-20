def validate_palindrome(s):
    val = list(s)
    left =0
    right = len(val)-1
    while(left < right):
        if (s[left] != s[right]) :
            return False
        left +=1
        right -=1
    return True
print(validate_palindrome("madam"))