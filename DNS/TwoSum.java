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
}