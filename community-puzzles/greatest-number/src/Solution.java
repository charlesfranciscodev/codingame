import java.util.*;
import java.util.stream.Collectors;

class Solution {
  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    int nbChars = in.nextInt();
    in.nextLine();
    String str = in.nextLine();
    System.err.println(str);
    String[] array = str.split(" ");
    List<String> list = new ArrayList<>(Arrays.asList(array));

    // Check for negative sign and remove it if present
    String negStr = "-";
    boolean negative = list.remove(negStr);

    // Check for the dot symbol and remove it if present
    final String DOT_STR = ".";
    boolean dot = list.remove(DOT_STR);

    List<Integer> digits = list.stream().map(Integer::valueOf).collect(Collectors.toList());

    String nbStr;
    // Sort and position the dot depending on the sign
    if (negative) {
      digits.sort(Integer::compareTo);
       nbStr = convert(digits);
      if (dot)
        nbStr = "-" + nbStr.charAt(0) + DOT_STR + nbStr.substring(1);
      else
        nbStr = "-" + nbStr;
    } else {
      digits.sort(Comparator.reverseOrder());
      nbStr = convert(digits);
      if (dot) {
        int lastIndex = nbStr.length() - 1;
        nbStr = nbStr.substring(0, lastIndex) + DOT_STR + nbStr.charAt(lastIndex);
      } // if
    } // else

    double number = Double.parseDouble(nbStr);

    String formatted;

    if (number == (long) number) {
      formatted = String.format("%d", (long) number);
    } else {
      formatted = String.format("%s", number);
    } // else

    System.out.println(formatted);
  } // main()

  static String convert(List<Integer> digits) {
    String nbStr = "";
    for (Integer i : digits)
      nbStr += String.valueOf(i);
    return nbStr;
  } // convert
} // Solution