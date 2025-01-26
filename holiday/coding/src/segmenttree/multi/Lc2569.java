package segmenttree.multi;

import java.util.ArrayList;
import java.util.Arrays;

import java.util.List;

public class Lc2569 {

    int[] cnt;
    boolean[] flip;
    int[] nums;


    public long[] handleQuery(int[] nums1, int[] nums2, int[][] queries) {
        cnt = new int[nums1.length * 4];
        flip = new boolean[nums1.length * 4];
        nums = nums1;
        build(1, 1, nums1.length);

        long tt = 0L;

        for (int i = 0; i < nums2.length; i++) {
            tt += nums2[i];
        }

        List<Long> tmp = new ArrayList<>();

        for (int i = 0; i < queries.length; i++) {
            int flag = queries[i][0];
            if (flag == 1){
                change(1, 1, nums1.length, queries[i][1]+1, queries[i][2]+1);
            }
            if (flag == 2){
                tt += query(1, 1, nums1.length, 1, nums1.length) * queries[i][1];
            }
            if (flag == 3){
                tmp.add(tt);
            }
        }

        long[] res = new long[tmp.size()];
        for (int i = 0; i < tmp.size(); i++) {
            res[i] = tmp.get(i);
        }
        return res;
    }

    private long query(int k, int l, int r, int left, int right) {
        if (l >= left && r <= right){
            return cnt[k];

        }

        pushDown(k, l, r);

        int ls = k * 2;
        int rs = k * 2;
        int mid = (l + r) / 2;

        long res = 0L;
        if (left <= mid){
            res += query(ls, l, mid, left, right);
        }
        if (right > mid){
           res += query(rs, mid + 1, r, left, right);
        }

        return res;
    }



    private void change(int k, int l, int r, int left, int right) {
        if (l >= left && r <= right){
            cnt[k] = (r - l + 1) - cnt[k];
            flip[k] = !flip[k];
            return;
        }

        pushDown(k, l, r);
        int ls = k * 2;
        int rs = k * 2 + 1;
        int mid = (l + r) / 2;

        if (left <= mid){
            change(ls, l, mid, left, right);
        }
        if (right > mid){
            change(rs, mid + 1, r, left, right);
        }

        cnt[k] = cnt[ls] + cnt[rs];

    }

    private void pushDown(int k, int l, int r) {
        if (!flip[k]){
            return;
        }
        int ls = k * 2;
        int rs = k * 2 + 1;
        int mid = (l + r) / 2;

        cnt[ls] = (mid - l + 1) - cnt[ls];
        cnt[rs] = (r - mid) - cnt[rs];

        flip[ls] = !flip[ls];
        flip[rs] = !flip[rs];

        flip[k] = false;
    }

    public void build(int k, int l, int r) {
        if (l == r){
            cnt[k] = nums[l-1];
            return;
        }

        int ls = k * 2;
        int rs = k * 2 + 1;
        int mid = (l + r) / 2;

        build(ls, l, mid);
        build(rs, mid+1, r);

        cnt[k] = cnt[ls] + cnt[rs];
    }


    public static void main(String[] args) {
        int[] a = {1,0,1};
        int[] b = {0,0,0};
        int[][] c = {{1,1,1},{2, 1, 0},{3,0,0}};
        long[] res = new Lc2569().handleQuery(a, b, c);
        System.out.println(Arrays.toString(res));;
    }

}
