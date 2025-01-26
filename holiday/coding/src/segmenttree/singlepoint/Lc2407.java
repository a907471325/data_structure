package segmenttree.singlepoint;

public class Lc2407 {
    int mx;
    int max[];


    public int lengthOfLIS(int[] nums, int k) {
        for (int num: nums){
            mx = Math.max(mx, num);
        }
        max = new int[mx * 4];
        int ans = 1;
        for (int num: nums){
            if (num == 1){
                update(1, 1, mx, num, 1);
                continue;
            }
            int cur = query(1, 1, mx, Math.max(num-k, 1), num - 1) + 1;
            ans = Math.max(cur, ans);
            update(1, 1, mx, num, cur);
        }
        return ans;
    }

    private int query(int k, int l, int r, int left, int right) {

        if (l >= left && r <= right){
            return max[k];
        }

        int ls = k * 2;
        int rs = k * 2 + 1;
        int mid = (l + r) / 2;

        int res = 0;
        if (left <= mid){
            res = Math.max(query(ls, l, mid, left, right), res);
        }
        if (right > mid){
            res = Math.max(query(rs, mid + 1, r, left, right), res);
        }
        return res;
    }

    private void update(int k, int l, int r, int idx, int val) {
        if (l == r){
            max[k] = val;
            return;
        }

        int ls = k * 2;
        int rs = k * 2 + 1;
        int mid = (l + r) / 2;
        if (idx <= mid){
            update(ls, l, mid, idx, val);
        }
        if (idx > mid){
            update(rs,  mid + 1, r, idx, val);
        }
        max[k] = Math.max(max[ls], max[rs]);
    }

    public static void main(String[] args) {
//        int[] a = {4,2,1,4,3,4,5,8,15};
//        int[] a = {7,4,5,1,8,12,4,7};
        int[] a = {1,5};
//        int k = 5;
        int k = 1;
        System.out.println(new Lc2407().lengthOfLIS(a, k));
    }
}
