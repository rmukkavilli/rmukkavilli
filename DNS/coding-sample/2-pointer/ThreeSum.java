
import java.util.*;

class ThreeSum {

    public static void main(String args[]) {
        int[][] numsArrs = {
            {-1, 0, 1, 2, -1, -4},
            {1, 2, 3, 4, 5},
            {0, 0, 0, 0},
            {-4, -1, -1, 0, 1, 2, 2},
            {-10, -7, -3, -1, 0, 3, 7, 10},
            {-3, -5, -7, -9}
        };

        for (int i = 0; i < numsArrs.length; i++) {
            int[] nums = numsArrs[i];
            System.out.println((i + 1) + ".\tnums: [" + Arrays.toString(nums));
            List<List<Integer>> result = threeSum(nums);
            System.out.println(new String(new char[100]).replace('\0', '-'));
            System.out.print("\n\tTriplets: ");
            System.out.println(result);
            System.out.println(new String(new char[100]).replace('\0', '-'));
        }

    }

    public static List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        int sum = 0;
        System.out.println(Arrays.toString(nums));
        Set<List<Integer>> list = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            if (i == 0 || nums[i] != nums[i - 1]) {
                int left = i + 1;
                int right = nums.length - 1;
                while (left < right) {
                    sum = nums[i] + nums[left] + nums[right];
                    if (sum < 0) {
                        left++;
                    } else if (sum > 0) {
                        right--;
                    } else {
                        list.add(Arrays.asList(nums[i], nums[left], nums[right]));
                        while (left < right && nums[left] == nums[left - 1]) {
                            left++;
                        }
                        while (right < nums.length-1 && nums[right] == nums[right - 1]) {
                            right--;
                        }
                    }

                }

            }
        }
        return new ArrayList<>(list);
    }

}
