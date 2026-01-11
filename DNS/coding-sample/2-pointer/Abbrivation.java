
/**
 * Validates whether a given abbreviation matches a word according to specific rules.
 * 
 * This class provides functionality to check if an abbreviation is a valid representation
 * of a word. The abbreviation rules are:
 * - Letters in the abbreviation must match the corresponding letters in the word (case-sensitive)
 * - Digits in the abbreviation represent the number of characters to skip in the word
 * - All characters in both the word and abbreviation must be consumed for a valid match
 * 
 * Example:
 * - Word: "internationalization", Abbreviation: "i18n" → true
 *   (i matches 'i', 18 skips 18 characters, n matches 'n')
 * 
 * @author Your Name
 * @version 1.0
 */

/**
 * Validates if the given abbreviation matches the given word.
 * 
 * The method iterates through both the word and abbreviation simultaneously:
 * - When a letter is encountered in the abbreviation, it must match the current
 *   character in the word exactly
 * - When digit(s) are encountered, they form a number representing how many
 *   characters to skip in the word
 * - The validation succeeds only if both strings are fully consumed
 * 
 * @param s the word string to validate against
 * @param abbr the abbreviation string to validate
 * @return true if the abbreviation is valid for the word, false otherwise
 * 
 * @example
 * validwordAbbrivation("internationalization", "i18n") returns true
 * validwordAbbrivation("apple", "a2ple") returns false
 */
class Abbrivation {

    public static void main(String args[]) {
        String s = "internationalization";
        String abbr = "i09n";
        //String abbr = "i18n";
        System.out.println(validwordAbbrivation(s, abbr));
    }

    public static boolean validwordAbbrivation(String s, String abbr) {
        int left = 0;
        int b = 0;
        while (left < s.length() && b < abbr.length()) {
            if (Character.isLetter(abbr.charAt(b))) {
                if (s.charAt(left) == abbr.charAt(b)) {
                    left++;
                    b++;
                } else if(abbr.charAt(b) == '0') {
                    return false;
                }
            } else if (Character.isDigit(abbr.charAt(b))) {
                String numStr = "";
                while (b < abbr.length() && Character.isDigit(abbr.charAt(b))) {
                    numStr += abbr.charAt(b);
                    b++;
                }
                int num = Integer.parseInt(numStr);
                left += num;
            }
        }
        return left == s.length() && b == abbr.length();
    }
}
