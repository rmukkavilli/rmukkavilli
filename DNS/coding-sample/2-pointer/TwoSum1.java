
import java.util.*;

class TwoSum1 {

    public static void main(String args[]) {
        List<Integer> list = new ArrayList<>();
        Collections.addAll(list, 5, 4, 3, 2);
        System.out.println(countPairs(list, 7));
    }

    public static int countPairs(List<Integer> nums, int target) {
        // 2,3,4,5 
        // 2,5 =7 (0)right --
        // 2,3 ==> 5 (1)
        // 2, 4 6(2)

        Collections.sort(nums);
        int sum = 0;
        int count = 0;
        int left = 0;
        int right = nums.size() - 1;
        while (left < right) {
            System.out.println(nums.get(left) + ": rigth : " + nums.get(right));
            if ((nums.get(left) + nums.get(right)) < target) {
                count = (right - left);
            } else {
                right--;
            }
        }
        return count;
    }
}
