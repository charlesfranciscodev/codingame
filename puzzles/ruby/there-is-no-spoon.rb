# Three coordinates: a node, its right neighbor, its bottom neighbor
# puts "0 0 1 0 0 1"

STDOUT.sync = true # DO NOT REMOVE

EMPTY_NEIGHBOR = "-1 -1 "
ZERO = '0'
DOT = '.'

@width = gets.to_i # the number of cells on the X axis
@height = gets.to_i # the number of cells on the Y axis
cells = Array.new(@height) {Array.new(@width, false)}
# Fill the array
STDERR.print("Cells: (#{@width} x #{@height}) \n")
@height.times do |i|
  line = gets.chomp # width characters, each either 0 or .
  @width.times do |j|
    if line[j] == ZERO
      cells[i][j] = true
    end
    STDERR.print(cells[i][j] ? ZERO : DOT)
  end
  STDERR.print("\n")
end

# loop trough the array to compute every node
@height.times do |i|
  @width.times do |j|
    node = cells[i][j]
    if node
      print("#{j} #{i} ")

    # Search for the right neighbor
    neighbor = false
    neighborWidth = j + 1
    while (!neighbor) && (neighborWidth < @width) do
      neighbor = cells[i][neighborWidth]
      if neighbor
        print("#{neighborWidth} #{i} ")
      end # if
      neighborWidth = neighborWidth + 1
    end # while

    if !neighbor
      print(EMPTY_NEIGHBOR)
    end # if

    # Search for the bottom neighbor
    neighbor = false # reset
    neighborHeight = i + 1
    while (!neighbor) && (neighborHeight < @height) do
      neighbor = cells[neighborHeight][j]
      if neighbor
        print("#{j} #{neighborHeight} ")
      end # if
      neighborHeight = neighborHeight + 1
    end # while

    if !neighbor
      print(EMPTY_NEIGHBOR)
    end # if

    # New cell
    print("\n")

    end # if
  end # width loop
end # height loop