package luogu;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;

public class p3373 {


    static class SegmentTree {

        long[] sum;
        long[] add;
        long[] mul;

        int[] arr;
        int mod;

        public SegmentTree(int[] nums, int mod) {
            this.arr = nums;
            this.mod = mod;
            this.sum = new long[nums.length * 4];
            this.add = new long[nums.length * 4];
            this.mul = new long[nums.length * 4];
            Arrays.fill(mul, 1);

            build(1, 1, nums.length);
        }

        public void build(int k, int left, int right){

            if (left == right){
                sum[k] = arr[left-1];
                return;
            }

            int ls = k * 2;
            int rs = ls + 1;
            int mid = (left + right) / 2;

            build(ls, left, mid);
            build(rs, mid+1, right);

            sum[k] = (sum[ls] + sum[rs]) % mod;

        }

        void pushDown(int k, int l, int r){



            int ls = k * 2;
            int rs = k * 2 + 1;
            int mid = (l + r) / 2;

            sum[ls] = (sum[ls] * mul[k] + (mid - l + 1) * add[k]) % mod;
            sum[rs] = (sum[rs] * mul[k] + (r - mid) * add[k]) % mod;

            mul[ls] = (mul[ls] * mul[k]) % mod;
            mul[rs] = (mul[rs] * mul[k]) % mod;

            add[ls] = (add[ls] * mul[k] + add[k]) % mod;
            add[rs] = (add[rs] * mul[k] + add[k]) % mod;

            add[k] = 0;
            mul[k] = 1;

        }

        long query(int k, int l, int r, int left, int right){
            if (l >= left && r <= right){
                return sum[k] % mod;
            }

            pushDown(k, l, r);
            int ls = k * 2;
            int rs = k * 2 + 1;
            int mid = (l + r) / 2;

            long res = 0L;
            if (left <= mid){
                res += query(ls, l, mid, left, right);
            }
            if (right > mid){
                res += query(rs, mid+1, r, left, right);
            }
            return res % mod;
        }

        void add(int k, int l, int r, int left, int right, int val){

            if (l >= left && r <= right){
                sum[k] = (sum[k] + (r - l + 1) * val) % mod;
                add[k] += val;
                return;
            }

            pushDown(k, l, r);
            int ls = k * 2;
            int rs = k * 2 + 1;
            int mid = (l + r) / 2;

            if (left <= mid){
                add(ls, l, mid, left, right, val);
            }
            if (right > mid){
                add(rs, mid+1, r, left, right, val);
            }

            sum[k] = (sum[ls] + sum[rs]) % mod;


        }

        void mul(int k, int l, int r, int left, int right, int val){

            if (l >= left && r <= right){
                sum[k] *= val;
                sum[k] = sum[k] % mod;
                add[k] *= val;
                mul[k] *= val;
                return;
            }

            pushDown(k, l, r);
            int ls = k * 2;
            int rs = k * 2 + 1;
            int mid = (l + r) / 2;

            if (left <= mid){
                mul(ls, l, mid, left, right, val);
            }
            if (right > mid){
                mul(rs, mid+1, r, left, right, val);
            }

            sum[k] = (sum[ls] + sum[rs]) % mod;

        }

    }

    public static int[] getArr(String line){

        String[] s = line.replace("\r\n", "").split(" ");
        int[] arr = new int[s.length];

        for (int i = 0; i < s.length; i++) {
            arr[i] = Integer.parseInt(s[i]);
        }

        return arr;
    }

    public static int[] getArr(StreamTokenizer tk, int n) throws IOException {

        int[] arr = new int[n];

        for (int i = 0; i < arr.length; i++) {
            tk.nextToken();
            arr[i] = (int)tk.nval;
        }

        return arr;
    }


    public static int nint(StreamTokenizer tk) throws IOException {
        tk.nextToken();
        return (int)tk.nval;
    }


    public static void main(String[] args) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer tk = new StreamTokenizer(reader);

        int n = nint(tk), q = nint(tk), mod = nint(tk);
        SegmentTree segmentTree = new SegmentTree(getArr(tk, n), mod);

        for (int i = 0; i < q; i++) {

            int flag = getArr(tk, 1)[0];
            int[] op;

            if (flag == 1){
                op = getArr(tk, 3);
                segmentTree.mul(1, 1, n, op[0], op[1], op[2]);
            }

            if (flag == 2){
                op = getArr(tk, 3);
                segmentTree.add(1, 1, n, op[0], op[1], op[2]);
            }

            if (flag == 3){
                op = getArr(tk, 2);
                System.out.println(segmentTree.query(1, 1, n, op[0], op[1]));
            }
        }

        reader.close();

    }



}
