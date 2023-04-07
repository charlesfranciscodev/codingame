import java.util.Scanner

fun main(args : Array<String>) {
  val input = Scanner(System.`in`)
  val n = input.nextInt()
  val reservationList = ArrayList<Task>()
  for (i in 0 until n) {
    val startDay = input.nextInt()
    val duration = input.nextInt()
    val task = Task(startDay, startDay + duration - 1)
    reservationList.add(task)
  }

  reservationList.sort()

  val carryList = ArrayList<Task>()
  carryList.add(reservationList[0])
  var prevIndex = 0
  for (i in 1 until n) {
    val task = reservationList[i]
    val prevTask = reservationList[prevIndex]
    // check if task doesn't overlap
    if (task.startDay > prevTask.endDay) {
      carryList.add(task)
      prevIndex = i
    }
  }

  println(carryList.size)
}

class Task(val startDay: Int, val endDay: Int) : Comparable<Task> {
  override fun compareTo(other: Task): Int {
    return endDay - other.endDay
  }
}
