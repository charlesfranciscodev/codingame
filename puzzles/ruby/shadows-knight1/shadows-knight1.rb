STDOUT.sync = true # DO NOT REMOVE
width, height = gets.split.map(&:to_i)
n = gets.to_i
x, y = gets.split.map(&:to_i) # Starting x,y position of Batman

minX = 0
maxX = width - 1
minY = 0
maxY = height - 1

loop {
  bomb_dir = gets.chomp

  case bomb_dir
    when "U"
      minX = maxX = x
      maxY = y - 1
    when "R"
      minX = x + 1
      minY = maxY = y
    when "D"
      minX = maxX = x
      minY = y + 1
    when "L"
      maxX = x - 1
      minY = maxY = y
    when "UR"
      minX = x + 1
      maxY = y - 1
    when "UL"
      maxX = x - 1
      maxY = y - 1
    when "DR"
      minX = x + 1
      minY = y + 1
    when "DL"
      maxX = x - 1
      minY = y + 1
  end

  x = (minX + maxX) / 2
  y = (minY + maxY) / 2
  puts("#{x} #{y}") # the location of the next window Batman should jump to.
}
