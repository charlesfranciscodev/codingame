n = gets.to_i # the number of temperatures to analyse
min = 5526
inputs = gets.split.map(&:to_i)
for t in inputs
  # t: a temperature expressed as an integer ranging from -273 to 5526
  if t.abs < min.abs || t.abs == min.abs && t > min
    min = t
  end
end

puts n == 0 ? 0 : min

