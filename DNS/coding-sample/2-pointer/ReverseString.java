import java.util.Arrays;
class ReverseString {
    public static void main(String args[]) {
        String a = "              Hello     World                     ";
        System.out.println(reverseString(a));
    }

    public static String reverseString(String a) {
        // convert String into String array
        String[] array = a.split("\\s+");
        System.out.println(Arrays.toString(array));
        int right = array.length -1;
        int i =0;
        while(i < right) {
            String temp = array[i];
            array[i] = array[right];
            array[right] = temp;
            i++;
            right--;
        }
            return String.join(" ", array);
        }
    }