import java.util.*

fun main(args : Array<String>) {
  val input = Scanner(System.`in`)
  val nbFloors = input.nextInt() // number of floors
  val width = input.nextInt() // width of the area
  val nbRounds = input.nextInt() // maximum number of rounds
  val exitFloor = input.nextInt() // floor on which the exit is found
  val exitPos = input.nextInt() // position of the exit on its floor
  val nbTotalClones = input.nextInt() // number of generated clones
  val nbAdditionalElevators = input.nextInt() // ignore (always zero)
  val nbElevators = input.nextInt() // number of elevators
  var elevators = Array(nbElevators + 1, {0})
  // For the last floor, we use the exit instead of an elevator.
  elevators[exitFloor] = exitPos

  for (i in 0 until nbElevators) {
    val elevatorFloor = input.nextInt() // floor on which this elevator is found
    val elevatorPos = input.nextInt() // position of the elevator on its floor
    elevators[elevatorFloor] = elevatorPos
  }

  // game loop
  while (true) {
    val cloneFloor = input.nextInt() // floor of the leading clone
    val clonePos = input.nextInt() // position of the leading clone on its floor
    val direction = input.next() // direction of the leading clone: LEFT or RIGHT

    if (cloneFloor == -1) {
      println("WAIT")
    } else if (direction.equals("LEFT") && clonePos < elevators[cloneFloor]) {
      println("BLOCK")
    } else if (direction.equals("RIGHT") && clonePos > elevators[cloneFloor]) {
      println("BLOCK")
    } else {
      println("WAIT")
    }
  }
}
