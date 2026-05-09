import java.util.Scanner

fun main(args: Array<String>) {
    val scanner = Scanner(System.`in`)
    while (true) {
        val enemy1 = scanner.next() // name of enemy 1
        val dist1 = scanner.nextInt() // distance to enemy 1
        val enemy2 = scanner.next() // name of enemy 2
        val dist2 = scanner.nextInt() // distance to enemy 2

        if (dist1 < dist2) {
            println(enemy1)
        } else {
            println(enemy2)
        }
    }
}
