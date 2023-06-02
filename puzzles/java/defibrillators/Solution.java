import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double lon = toRadians(input.next());
        double lat = toRadians(input.next());
        int n = input.nextInt();
        if (input.hasNextLine()) {
            input.nextLine();
        }
        double min = Double.POSITIVE_INFINITY;
        String name = "";

        for (int i = 0; i < n; i++) {
            String[] defib = input.nextLine().split(";");
            double defibLon = toRadians(defib[4]);
            double defibLat = toRadians(defib[5]);
            double x = (defibLon - lon) * Math.cos((lat + defibLat) / 2);
            double y = defibLat - lat;
            double distance = Math.hypot(x, y) * 6371;
            if (distance < min) {
                min = distance;
                name = defib[1];
            }
        }

        System.out.println(name);
    }

    // Convert degrees to radians
    private static double toRadians(String angle) {
        return Math.toRadians(Double.parseDouble(angle.replace(',', '.')));
    }
}
