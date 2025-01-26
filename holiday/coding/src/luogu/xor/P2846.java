package luogu.xor;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class P2846 {

    static class SegmentTree {

        long[] sum;
        boolean[] flip;


        public SegmentTree(int n ) {
            this.sum = new long[n * 4];
            this.flip = new boolean[n * 4];

            build(1, 1, n);
        }

        public void build(int k, int left, int right){

            if (left == right){
                sum[k] = 0;
                return;
            }

            int ls = k * 2;
            int rs = ls + 1;
            int mid = (left + right) / 2;

            build(ls, left, mid);
            build(rs, mid+1, right);

            sum[k] = (sum[ls] + sum[rs]);

        }

        void pushDown(int k, int l, int r){
            if (flip[k] == false){
                return;
            }

            int ls = k * 2;
            int rs = k * 2 + 1;
            int mid = (l + r) / 2;

            sum[ls] = (mid - l + 1) - sum[ls];
            sum[rs] = (r - mid) - sum[rs];

            flip[ls] = !flip[ls];
            flip[rs] = !flip[rs];

            flip[k] = false;

        }

        long query(int k, int l, int r, int left, int right){
            if (l >= left && r <= right){
                return sum[k];
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
            return res ;
        }

        void change(int k, int l, int r, int left, int right){

            if (l >= left && r <= right){
                sum[k] = (r - l + 1) - sum[k];
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
                change(rs, mid+1, r, left, right);
            }

            sum[k] = sum[ls] + sum[rs];

        }

    }


    public static int[] getArr(StreamTokenizer tk, int n) throws IOException {

        int[] arr = new int[n];

        for (int i = 0; i < arr.length; i++) {
            tk.nextToken();
            arr[i] = Integer.parseInt(tk.sval);
        }

        return arr;
    }

    public static int[] getArrFromDouble(StreamTokenizer tk, int n) throws IOException {

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

    public static int[] nStringArr(StreamTokenizer tk) throws IOException {

        tk.nextToken();
        String val = tk.sval;
        int[] arr = new int[val.length()];
        for (int i = 0; i < val.length(); i++) {
            arr[i] = Integer.parseInt(val.charAt(i) + "");
        }

        return arr;
    }


    public static void main(String[] args) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer tk = new StreamTokenizer(reader);

        int n = nint(tk), q = nint(tk);

        SegmentTree segmentTree = new SegmentTree(n);

        for (int i = 0; i < q; i++) {

            int flag = getArrFromDouble(tk, 1)[0];
            int[] op;

            if (flag == 0){
                op = getArrFromDouble(tk, 2);
                segmentTree.change(1, 1, n, op[0], op[1]);
            }

            if (flag == 1){
                op = getArrFromDouble(tk, 2);
                System.out.println(segmentTree.query(1, 1, n, op[0], op[1]));
            }
        }

        reader.close();

    }

}
