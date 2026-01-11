import java.util.*;
class Stomogramatic {
    public static void main(String args[]) {
        String a = "188"; //180
        System.out.println(isStomogramatic(a));
    }

    public static boolean isStomogramatic(String s) {
        Map<Character, Character> map = new HashMap<>();
        map.put('0', '0');
        map.put('1', '1');
        map.put('8', '8');
        map.put('6', '9');
        map.put('9', '6');
        int left = 0;
        int right = s.length() -1;
        while (left <=right) {
            if (!map.containsKey(s.charAt(left)) || s.charAt(left) !=s.charAt(right)) {
                return false;
            }

           left++;
           right--;
        }
        
        return true;
    }
}