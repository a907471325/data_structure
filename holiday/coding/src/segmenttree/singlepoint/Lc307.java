package segmenttree.singlepoint;

public class Lc307 {

    static class SegmentTree {

        long[] tree;
        int[] arr;

        public SegmentTree(int[] arr) {
            this.arr = arr;
            this.tree = new long[arr.length * 4];
            build(1, 1, arr.length);
        }

        public void build(int k, int l, int r) {
            if (l == r) {
                tree[k] = arr[l - 1];
                return;
            }
            int ls = k * 2;
            int rs = k * 2 + 1;
            int mid = (l + r) / 2;

            build(ls, l, mid);
            build(rs, mid + 1, r);
            tree[k] = tree[ls] + tree[rs];
        }

        public void update(int k, int l, int r, int idx, int val){
            if (l == r){
                arr[idx-1] = val;
                tree[k] = val;
                return;
            }

            int ls = k * 2;
            int rs = k * 2 + 1;
            int mid = (l + r) / 2;

            if (idx <= mid){
                update(ls, l, mid, idx, val);
            }

            if (mid < idx){
                update(rs, mid + 1, r, idx, val);
            }

            tree[k] = tree[ls] + tree[rs];
        }

        public long query(int k, int l, int r, int ql, int qr){
            if (l >= ql && r <= qr){
                return tree[k];
            }

            int ls = k * 2;
            int rs = k * 2 + 1;
            int mid = (l + r) / 2;

            long res = 0L;
            if (ql <= mid){
                res += query(ls, l, mid, ql, qr);
            }
            if (mid < qr){
                res += query(rs, mid + 1, r, ql, qr);
            }
            return res;
        }
    }


    static class NumArray {

        SegmentTree segmentTree;

        public NumArray(int[] nums) {
            this.segmentTree = new SegmentTree(nums);
        }

        public void update(int index, int val) {
            segmentTree.update(1, 1, segmentTree.arr.length, index+1, val);
        }

        public int sumRange(int left, int right) {
            return (int)segmentTree.query(1, 1, segmentTree.arr.length, left+1, right+1);
        }
    }

    public static void main(String[] args) {
        int[] arr = {1, 3, 5};
        NumArray numArray = new NumArray(arr);
        System.out.println(numArray.sumRange(0, 2));
        numArray.update(1, 2);
        System.out.println(numArray.sumRange(0, 2));
    }





}