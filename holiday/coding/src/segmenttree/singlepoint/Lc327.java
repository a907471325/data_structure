package segmenttree.singlepoint;

import java.util.*;

public class Lc327 {

    int[] sum;

    //  lo <= pj - pi <= hi;
    // pj - hi <= pi <= pj - lo

    public int countRangeSum(int[] nums, int lower, int upper) {

        int n = nums.length;

        long[] psums = new long[n + 1];

        long tot = 0;

        for (int i = 0; i < n; i++) {
            tot += nums[i];
            psums[i+1] = tot;
        }

        List<Long> allValues = new ArrayList<>();

        for (long val: psums){
            allValues.add(val-lower);
            allValues.add(val-upper);
            allValues.add(val);
        }

        Collections.sort(allValues);

        Map<Long, Integer> ord = new HashMap<>();

        for (long s: allValues){
            if (!ord.containsKey(s)){
                ord.put(s, ord.size()+1);
            }
        }


        int res = 0;
        sum = new int[4 * ord.size()];
        for (long tt: psums) {
            int cnt = query(1, 1, ord.size(), ord.get(tt-upper), ord.get(tt-lower));
            add(1, 1, ord.size(), ord.get(tt));
            res += cnt;
        }
        return res;

    }

    private int query(int k, int l, int r, int left, int right) {
        if (left <= l && r <= right){
            return sum[k];
        }

        int m = (l + r) / 2;
        int ls = k * 2;
        int rs = k * 2 + 1;

        int res = 0;
        if (left <= m){
            res += query(ls, l,  m, left, right);
        }
        if (m < right){
            res += query(rs, m+1, r, left, right);
        }

        return res;
    }

    private void add(int k, int l, int r, int idx) {

        if (l == r){
            sum[k] += 1;
            return;
        }

        int m = (l + r) / 2;
        int ls = k * 2;
        int rs = k * 2 + 1;

        if (idx <= m){
            add(ls, l,  m, idx);
        } else{
            add(rs, m+1, r, idx);
        }

        sum[k] = sum[ls] + sum[rs];
    }

    public static void main(String[] args) {
        int[] nums = {-2,5,-1};
        int lower = -2;
        int upper = 2;

        System.out.println(new Lc327().countRangeSum(nums, lower, upper));
    }


}
