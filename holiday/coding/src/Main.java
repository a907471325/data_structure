import java.util.*;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {


    public static void main(String[] args) {
        List<Character>[] bucket = new ArrayList[1];
        bucket[0] = new ArrayList<>();
        bucket[0].add('c');
        System.out.println(bucket[0].get(0));

//        List<Integer> list = new ArrayList<>();
        List<String> list = new ArrayList<>();
//        list.add(0, 1);
//        int[] s = {};

        String[] s = {};
        Collections.addAll(list, s);
        //TIP Press <shortcut actionId="ShowIntentionActions"/> with your caret at the highlighted text
        // to see how IntelliJ IDEA suggests fixing it.
        System.out.printf("Hello and welcome!");

        for (int i = 1; i <= 5; i++) {
            //TIP Press <shortcut actionId="Debug"/> to start debugging your code. We have set one <icon src="AllIcons.Debugger.Db_set_breakpoint"/> breakpoint
            // for you, but you can always add more by pressing <shortcut actionId="ToggleLineBreakpoint"/>.
            System.out.println("i = " + i);
        }

        int[] ans = null;
        Queue<Integer> ob = new PriorityQueue<>((o, v)-> v - o);
//        int[] res = new int[]{};
        String[] res = new String[]{"3","6","7","10"};
        ans = new int[]{1, 2};
        Arrays.sort(res);
        System.out.println(Arrays.toString(res));
        System.out.println("1".compareTo("2"));

        new Random().nextInt(11);

    }
}