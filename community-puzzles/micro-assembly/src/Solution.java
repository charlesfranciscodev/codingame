import java.util.*;

class Solution {
  static int[] registers;
  static String[] instructions;
  static int curLine = 0; // current line
  static final String names = "abcd"; // register names

  public static void main(String args[]) {
    final int NB_REGISTERS = 4;
    Scanner in = new Scanner(System.in);
    registers = new int[NB_REGISTERS]; // Register values a b c d
    for (int i = 0; i < NB_REGISTERS; ++i)
      registers[i] = in.nextInt();

    int nbLines = in.nextInt();
    in.nextLine();
    instructions = new String[nbLines];
    for (int i = 0; i < nbLines; ++i)
      instructions[i] = in.nextLine();

    do {
      String line = instructions[curLine];
      interpret(line);
      System.err.println(curLine + " " + line);
      printRegisters();
    } while (curLine != nbLines);

    String output = "";
    for (int register : registers)
      output += String.valueOf(register) + " ";

    System.out.println(output.trim()); // "a b c d"
  } // main()

  static void interpret(String line) {
    String[] instruction = line.split(" ");
    switch (instruction[0]) {
      case "MOV": move(instruction); ++curLine; break;
      case "ADD": add(instruction);  ++curLine; break;
      case "SUB": sub(instruction);  ++curLine; break;
      case "JNE": jumpNotEqual(instruction);    break;
    } // switch
  } // interpret()

  static void move(String[] instruction) {
    int dest = index(instruction[1]);
    String value = instruction[2];
    if (names.contains(value)) {
      int source = index(value);
      registers[dest] = registers[source];
    } else {
      registers[dest] = Integer.parseInt(value);
    } // else
  } // move

  static void operation(String[] instruction, int sign) {
    int result;

    int dest = index(instruction[1]);
    String value = instruction[2];
    if (names.contains(value)) {
      int source = index(value);
      result = registers[source];
    } else {
      result = Integer.parseInt(value);
    } // else

    value = instruction[3];
    if (names.contains(value)) {
      int source = index(value);
      result += sign * registers[source];
    } else {
      result += sign * Integer.parseInt(value);
    } // else

    registers[dest] = result;
  } // operation()

  static void add(String[] instruction) {
    operation(instruction, 1);
  } // add()

  static void sub(String[] instruction) {
    operation(instruction, -1);
  } // sub()

  static void jumpNotEqual(String[] instruction) {
    int operand1 = registers[index(instruction[2])];
    int operand2;
    String value2 = instruction[3];
    if (names.contains(value2))
      operand2 = registers[index(value2)];
    else
      operand2 = Integer.parseInt(value2);

    if (operand1 != operand2)
      curLine = Integer.parseInt(instruction[1]);
    else
      ++curLine;
  } // jumpNotEqual()

  static int index(String register) {
    return Character.toLowerCase(register.charAt(0)) -  'a';
  } // index()

  static void printRegisters() {
    String output = "";
    for (int register : registers)
      output += String.valueOf(register) + " ";

    System.err.println(output.trim()); // "a b c d"
  } // printRegisters()
} // Solution