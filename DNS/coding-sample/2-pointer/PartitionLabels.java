
// / **
//  * You are given a string s. Your task is to divide the string into as many parts as possible such that each letter appears in at most one part.

// In other words, no character should occur in more than one partition. After concatenating all parts in order, the result should be the original string s.

// For example, given s = "bcbcdd", a valid partition is ["bcbc", "dd"]. However, partitions like ["bcb", "cdd"] or ["bc", "bc", "dd"] are invalid because some letters appear in multiple parts.

// Return a list of integers representing the sizes of these partitions.
//  ** /
import java.util.*;
/**
 * TC : O(n)
 * SC : O(1)
 */
class PartitionLabels {
    public static void main(String args[]) {
        String a = "bcbcdd";
        System.out.println(partitionLabels(a));

    }

    public static List<Integer> partitionLabels(String a) {

        // find positions of each charcter in the string where its last position is
        int[] lastOccurence = new int[26];
        for (int i=0; i<a.length(); i++) {
            lastOccurence[a.charAt(i) - 'a'] = i;
        }

        int positionStart = 0;
        int positionEnd = 0;
        ArrayList<Integer> list = new ArrayList<>();
        for (int i=0; i<a.length(); i++) {
            // if character at i is matching the lastOccurence update positionEnd
            positionEnd = Math.max(positionEnd, lastOccurence[a.charAt(i)- 'a']);
            // Once i reaches positionEnd then update list with i -positionStart + 1
            // update positionStart to  i+ 1  to start with next character. .
             
            if (i == positionEnd) {
                positionStart = (i - positionStart) + 1;
                list.add(positionStart);
                positionStart = i+1;
            }

        }
        return list;
    }

}