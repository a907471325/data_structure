package luogu;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

public class template {


    public static int[] getArr(String line, int n){

        int[] arr = new int[n];

        String[] s = line.replace("\r\n", "").split(" ");
        for (int i = 0; i < s.length; i++) {
            arr[i] = Integer.parseInt(s[i]);
        }

        return arr;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader cin = new BufferedReader(new InputStreamReader(System.in));

        cin.close();
    }

    public static void main2(String[] args) throws Exception {
        Scanner cin = new Scanner(System.in);
        int a = cin.nextInt();
        int b = cin.nextInt();
        System.out.println(a+b);
    }
}
