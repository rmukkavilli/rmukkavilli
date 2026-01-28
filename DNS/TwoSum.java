import java.util.Arrays;
class TwoSum {
    public static void main(String args[]) {
        //int[] nums = {-1, 0, 1, 2, -1, -4};
        int[] nums1 = {4,2,1};
        int[] result = twoSum(nums1, 8);
        System.out.println(Arrays.toString(result));
    }
    private static int[] twoSum(int[] nums, int target) {
        Arrays.sort(nums);
       int left = 0;
       int right = nums.length -1;
       int sum = 0;
       while (left < right) {
        sum = nums[left] + nums[right];
        if (sum > target) right--;
        if (sum < target) left++;
        if (sum == target) {
            return new int[] {left, right};
        }
       }
       return new int[0];
    }

    /** O(1) and O(N) use Hash map */
    private static int[] twoSum1(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i];
        if (map.containsKey(complement)) {
            return new int[] {map.get(complement), i};  // original indices
        }
        map.put(nums[i], i);
    }
    return new int[0];
}
}