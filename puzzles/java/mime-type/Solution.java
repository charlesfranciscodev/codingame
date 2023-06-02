import java.util.HashMap;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int nbElements = input.nextInt(); // Number of elements which make up the association table.
        int nbNames = input.nextInt(); // Number of file names to be analyzed.
        HashMap<String, String> table = new HashMap<String, String>();

        for (int i = 0; i < nbElements; i++) {
            String extension = input.next().toLowerCase(); // file extension
            String type = input.next(); // MIME type.
            table.put(extension, type);
        }
        input.nextLine();

        for (int i = 0; i < nbNames; i++) {
            String name = input.nextLine().toLowerCase(); // One file name per line.
            int dotIndex = name.lastIndexOf('.');
            if (dotIndex == -1 || dotIndex == name.length() - 1) {
                System.out.println("UNKNOWN");
            } else {
                String extension = name.substring(dotIndex + 1).toLowerCase();
                if (table.containsKey(extension)) {
                    System.out.println(table.get(extension));
                } else {
                    System.out.println("UNKNOWN");
                }
            }
        }
    }
}
