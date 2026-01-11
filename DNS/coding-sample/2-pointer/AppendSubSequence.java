class AppendSubSequence {
    public static void main(String args[]) {
        String s = "axbycz";
        String target = "abcde";
        System.out.println(findAppendSequence(s, target));
    }

/**
 * Idea is for any given orig String s and target string, traverse through both Strings 
 * Parelly using 2 pointer source_index and target_index pointing to 0 and through n.
 * if character at source_idex and target_index value are same increment both pointers
 * otherwise increment source pointer alone as we wanted traverse once the entire array
 * finally target_length - target_idex should give us the answer
 * 
 * COMPEXITY :
 * TIME :  O(S+t) ~= O(N)
 * SPACE : O(1)
 */
    public static int findAppendSequence(String s, String target) {
        int orig_index = 0; 
        int target_index = 0;
        int r = s.length();
        int target_r = target.length();
        while(orig_index < r && target_index < target_r)  {
            if (s.charAt(orig_index) == target.charAt(target_index)) {
                target_index++;
            }  
                orig_index++;
            
        }
        System.out.println("target_r" + target_r + "target_index" + target_index);
                return target_r - target_index;
    }
}