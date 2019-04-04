import java.util.*

fun main(args: Array<String>) {
  // Read the game info
  val `in` = Scanner(System.`in`)
  val width = `in`.nextInt()
  val height = `in`.nextInt()

  val board = Board(height, width)

  for (y in 0 until height) {
    val row = `in`.next()
    for (x in 0 until width) {
      val c = row[x]
      val cell = board.grid!![y][x]
      cell?.c = c
      if (c == Cell.START) {
        board.start = cell
      }
    }
  }

  bfs(board)
}

fun bfs(board: Board) {
  val queue = LinkedList<Cell>()
  var current: Cell
  val cell = Cell(board.start!!.x, board.start!!.y)
  cell.isMarked = true
  queue.add(cell)

  while (!queue.isEmpty()) {
    current = queue.remove()
    for (neighbor in board.neighbors(current)) {
      neighbor!!.isMarked = true
      neighbor!!.prev = current
      if (neighbor!!.c == Cell.FINISH) {
        val path = Stack<Cell>()
        path.push(neighbor)
        var current: Cell? = neighbor
        while (!current!!.prev!!.equals(board.start)) {
          current = current.prev
          path.push(current)
        }
        System.out.println(path.size)
        return
      } else {
        queue.add(neighbor)
      }
    }
  }
  System.out.println("Impossible")
}

class Board(var height: Int, var width: Int) {
  var grid: Array<Array<Cell?>>? = null
  var start: Cell? = null // for BFS

  init {
    grid = Array(height) { arrayOfNulls<Cell>(width) } // [y][x]

    for (y in 0 until height) {
      for (x in 0 until width) {
        grid!![y][x] = Cell(x, y)
      }
    }
  }

  // at most 8 options around the knight
  fun neighbors(cell: Cell): ArrayList<Cell> {
    val list = ArrayList<Cell>()
    var x = cell.x + 2
    var y = cell.y + 1
    add(list, x, y)

    x = cell.x + 1
    y = cell.y + 2
    add(list, x, y)

    x = cell.x - 1
    y = cell.y + 2
    add(list, x, y)

    x = cell.x - 2
    y = cell.y + 1
    add(list, x, y)

    // next 4
    x = cell.x - 2
    y = cell.y - 1
    add(list, x, y)

    x = cell.x - 1
    y = cell.y - 2
    add(list, x, y)

    x = cell.x + 1
    y = cell.y - 2
    add(list, x, y)

    x = cell.x + 2
    y = cell.y - 1
    add(list, x, y)

    return list
  }

  fun add(list: ArrayList<Cell>, x: Int, y: Int) {
    if (isValid(x, y)) {
      val cell = grid!![y][x]
      if (isValid(cell)) {
        if (!(cell!!.isMarked)) {
          list.add(cell) 
        }
      }
    }
  }

  fun isValid(x: Int, y: Int): Boolean {
    return 0 <= x && x < width && 0 <= y && y < height
  }

  fun isValid(cell: Cell?): Boolean {
    return cell?.c != Cell.WALL // avoid walls
  }
} // Maze

class Cell(var x: Int, var y: Int) {
  // for BFS
  var prev: Cell? = null
  var isMarked: Boolean = false

  var c: Char = ' ' // type of the cell
  
  override fun equals(other: Any?): Boolean {
    val cell = other as Cell?
    return x == cell!!.x && y == cell!!.y
  }

  companion object {
    // Possible types of cells
    val WALL = '#'
    val START = 'B'
    val FINISH = 'E'
  }
}
