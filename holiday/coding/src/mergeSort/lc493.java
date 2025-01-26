package mergeSort;

import java.util.Arrays;

public class lc493 {

    static int ans;

    public int reversePairs(int[] nums) {
        ans = 0;
        helper(nums, 0, nums.length-1);
        return ans;
    }

    public int[] helper(int[] nums, int l, int r){
        if (l > r){
            return null;
        }
        if (l == r){
            return new int[]{nums[l]};
        }
        int m = (l + r) / 2;
        int[] lp = helper(nums, l, m);
        int[] rp = helper(nums, m+1, r);
        countPair(lp, rp);
        return merge(lp, rp);
    }

    public void countPair(int[] left, int[] right){
        if (left == null){
            return;
        }
        if (right == null){
            return;
        }

        int n = left.length;
        int m = right.length;

        int i = 0, j = 0;
        while (i < n || j < m){
            if(i < n && j < m){
                if (left[i] > 2 * (long)right[j]){
                    i++;
                    ans += m - j;
                } else{
                    j++;
                }
            } else if (i < n){
                i++;
            } else if (j < m){
                j++;
            }

        }
    }

    public int[] merge(int[] left, int[] right){
        if (left == null){
            return right;
        }
        if (right == null){
            return left;
        }

        int n = left.length;
        int m = right.length;
        int[] res = new int[n+m];

        int i = 0, j = 0, k = 0;

        while (i < n || j < m){
            if(i < n && j < m){
                if (left[i] >= right[j]){
                    res[k] = left[i];
                    i++;
                } else{
                    res[k] = right[j];
                    j++;
                }
            } else if (i < n){
                res[k] = left[i];
                i++;
            } else if (j < m){
                res[k] = right[j];
                j++;
            }
            k++;
        }
        return res;

    }


    public static void main(String[] args) {
//        int[] arr = {1,3,2,3,1};
//        int[] arr = {2,4,3,5,1};
//        int[] arr = {2,3,1};
        int[] arr = {2147483647,2147483647,2147483647,2147483647,2147483647,2147483647};
        System.out.println(new lc493().reversePairs(arr));
    }
}
