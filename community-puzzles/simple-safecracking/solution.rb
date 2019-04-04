def rot1(message)
  message.tr('A-Za-z', 'B-ZAb-za')
end

def numeral(message)
  hash = {
    'zero' => 0, 'one' => 1, 'two' => 2, 'three' => 3, 'four' => 4,
    'five' => 5, 'six' => 6, 'seven' => 7, 'eight' => 8, 'nine' => 9
  }
  size = "The safe combination is: ".size
  combination = message[size, message.size]
  STDERR.puts combination
  table = combination.split("-")
  table.each { |digit|
    print hash[digit]
  }
end

msg = gets.chomp

until msg[0, 3] == "The" do
  msg = rot1(msg)
end

STDERR.puts msg

numeral(msg)