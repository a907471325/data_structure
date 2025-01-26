package luogu;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class p3372 {

    static class SegmentTree {

        long[] sum;
        int[] lazy;
        int[] arr;

        public SegmentTree() {
        }

        public void build(int k, int left, int right){

            if (left == right){
                sum[k] = arr[left-1];
                return;
            }

            int mid = (left + right) / 2;
            int lc = k * 2;
            int rc = k * 2 + 1;
//        System.out.println(String.format("%s, %s, %s", lc, rc, mid));
            build(lc, left, mid);
            build(rc, mid + 1, right);
            sum[k] = sum[lc] + sum[rc];
        }

        void pushDown(int k, int l, int r){
            int m = (l + r) / 2;
            sum[k*2] += lazy[k] * (m - l + 1);
            sum[k*2 + 1] += lazy[k] * (r - m);

            lazy[k * 2] += lazy[k];
            lazy[k * 2 + 1] += lazy[k];
            lazy[k] = 0;

        }

        long query(int k, int l, int r, int left, int right){

            if (left <= l && right >= r){
                return sum[k];
            }

            if (lazy[k] != 0){
                pushDown(k, l, r);
            }
            int mid = (l + r) / 2;
            int kl = k * 2;
            int kr = k * 2 + 1;
            long res = 0L;
            if (left <= mid){
                res += query(kl, l, mid, left, right);
            }
            if (right > mid){
                res += query(kr, mid+1, r, left, right);
            }

            return res;
        }

        void modify(int k, int l, int r, int left, int right, int val){
            if (left <= l && right >= r){
                sum[k] += (long) (r - l + 1) * val;
                lazy[k] += val;
                return;
            }

            if (lazy[k] != 0){
                pushDown(k, l, r);
            }
            int mid = (l + r) / 2;
            int lc = k * 2;
            int rc = k * 2 + 1;

            if (left <= mid){
                modify(lc, l, mid, left, right, val);
            }
            if (right > mid){
                modify(rc, mid + 1, r, left, right, val);
            }
            sum[k] = sum[lc] + sum[rc];
        }

        public long[] getSum() {
            return sum;
        }

        public void setSum(long[] sum) {
            this.sum = sum;
        }

        public int[] getLazy() {
            return lazy;
        }

        public void setLazy(int[] lazy) {
            this.lazy = lazy;
        }

        public int[] getArr() {
            return arr;
        }

        public void setArr(int[] arr) {
            this.arr = arr;
        }
    }



    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().replace("\r\n", "").split(" ");
        int n1 = Integer.parseInt(s[0]), n2 = Integer.parseInt(s[1]);

        SegmentTree tree = new SegmentTree();
        tree.setArr(getArr(br.readLine(), n1));
        tree.setSum(new long[n1 * 4]);
        tree.setLazy(new int[n1 * 4]);

        tree.build(1, 1, n1);

        int[] op;
        for (int i = 0; i < n2; i++) {
            op = getArr(br.readLine().replace("\r\n", ""), 4);
            if (op[0] == 1){
                tree.modify(1, 1, n1, op[1], op[2], op[3]);
            } else if (op[0] == 2){
                long query = tree.query(1, 1, n1, op[1], op[2]);
                System.out.println(query);
            }

        }
        br.close();
//        System.out.println(Arrays.toString(arr));

    }



    public static int[] getArr(String line, int n){

        int[] arr = new int[n];

        String[] s = line.split(" ");
        for (int i = 0; i < s.length; i++) {
            arr[i] = Integer.parseInt(s[i]);
        }

        return arr;
    }
}
