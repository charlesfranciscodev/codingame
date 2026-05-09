l = gets.to_i
h = gets.to_i
t = gets.chomp

# Create a hash map to store the ASCII art for each character
characters = {}
row = "" # Initialize row as an empty string
(0...h).each do
  row = gets.chomp
  (0..26).each do |i|
    if i < 26
      character = ('A'.ord + i).chr
    else
      character = '?'
    end
    characters[character] ||= []
    characters[character] << row[(i * l)...((i + 1) * l)]
  end
end

# Print the text T in ASCII art
(0...h).each do |i|
  t.each_char do |char|
    char = char.upcase
    if characters.key?(char)
      print characters[char][i]
    else
      print characters['?'][i]
    end
  end
  puts
end
