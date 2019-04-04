@width = gets.to_i # the width of a letter represented in ASCII art
@height = gets.to_i # the height of a letter represented in ASCII art.
@text = gets.chomp.upcase

asciiArt = Array.new # the characters A to Z and ? represented in ASCII art.

@height.times do
  row = gets.chomp
  asciiArt.push(row)
end

# Prints the letter for every height level
asciiArt.each do |row|
  @text.each_char { |c|
    ascii = c.ord
    position = ascii - 'A'.ord
    unless position.between?(0, 25)
      position = 26
    end
    column = position * @width
    for i in column..(column + @width - 1) do
      print row[i]
    end
  }
  print "\n"
end
