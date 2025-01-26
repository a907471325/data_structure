package pq;

import java.util.*;

public class lc407TrappingRainWater2 {

    static class Node{
        int loc;
        int height;

        public Node(int loc, int height){
            this.loc = loc;
            this.height = height;
        }

    }


    public static int trapRainWater(int[][] arr) {
        int m = arr.length, n = arr[0].length;
        Comparator<Node> cmp = Comparator.comparingInt(o -> o.height);
        Queue<Node> q = new PriorityQueue<>(cmp);

        int[][] dirs = {{0,1}, {0,-1}, {1,0}, {-1,0}};

        int[][] vis = new int[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 || i == m - 1 || j == 0 || j == n - 1) {
                    vis[i][j] = 1;
                    q.add(new Node(i * n + j, arr[i][j]));
                }
            }
        }

        int res = 0;
        while (!q.isEmpty()){
            Node cur = q.poll();
            for (int i = 0; i < 4; i++) {
                int cx = cur.loc / n, cy = cur.loc % n;
                int nx = cx + dirs[i][0], ny = cy + dirs[i][1];
                if ((nx < 0 || nx == m || ny < 0 || ny == n) || vis[nx][ny] == 1){
                    continue;
                }
                if (arr[nx][ny] < cur.height){
                    res += cur.height - arr[nx][ny];
                }
                vis[nx][ny] = 1;
                q.add(new Node(nx * n + ny, Math.max(arr[nx][ny], cur.height)));
            }
        }


        return res;
    }

    public static void main(String[] args) {
        int[][] arr = {{1,4,3,1,3,2},{3,2,1,3,2,4},{2,3,3,2,3,1}};
        System.out.println(trapRainWater(arr));
    }

}
