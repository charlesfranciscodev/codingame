horses = []
min = 10000000
n = gets.to_i
n.times {
  horses.push(gets.to_i)
}

horses.sort!

for i in 0..(n - 2)
  diff = horses[i + 1] - horses[i]
  min = diff if diff < min
end

puts min
