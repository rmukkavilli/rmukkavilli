
class CheckPalindrome {
    public static void main(String[] args) {
        String s = "A man, a plan, a canal: Panama";
        System.out.println(isPalindrome(s));
    }

    public static boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        if (s.length() == 0) return true;
        while(left < right) {
            // while a character exist and character is not a letter or digit move to next character
            while (left <right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }
            // While right exist and character is not a letter or digit move to next character
            while(left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }
            if (Character.toLowerCase(s.charAt(left++)) != Character.toLowerCase(s.charAt(right--))) {
                return false;
            }
        }
    return true;
    }
}
