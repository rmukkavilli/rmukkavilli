# Tin O(N) and Space O(1)
def valid_palindrom(s):
    s = s.lower()
    print(s)
    left = 0
    right = len(s)-1
    while left < right:
         # left < right check otherwise strings with only special characters can crash.
         while left < right and not s[left].isalnum():
            left +=1
            
         while left < right and not s[right].isalnum():
            right -=1
            
         print(s[left] , "-", s[right])
         if s[left] != s[right]:
            return False

         left +=1
         right-=1
    return True


s = "A man,:, a plan, ,:a canal: Panama"
print(valid_palindrom(s))