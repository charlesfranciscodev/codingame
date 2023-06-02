import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        ArrayList<Integer> strengths = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            strengths.add(input.nextInt());
        }

        Collections.sort(strengths);

        int min = 10000000;
        for (int i = 0; i < n - 1; i++) {
            int diff = strengths.get(i + 1) - strengths.get(i);
            if (diff < min) {
                min = diff;
            }
        }

        System.out.println(min);
    }
}
