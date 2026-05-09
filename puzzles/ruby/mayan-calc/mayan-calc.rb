BASE = 20

@width, @height = gets.split.map(&:to_i) # the width/heigth of a mayan numeral
mayan_numerals = Array.new # the numbers 0 to 19 represented in mayan numerals
@mayan_hash = Hash.new # the numbers 0 to 19 represented in mayan numerals
num1 = 0
num2 = 0
result = 0

def read_num
  num_numeral = '' # mayan digit
  num_array = Array.new # the number read
  nb_lines = gets.to_i # the amount of lines of the number.

  nb_lines.times do |i|
    num_numeral += "#{gets.chomp}\n"
    if (i % @width) == (@width - 1) # if this is the last line
      num_array.push(@mayan_hash.fetch(num_numeral))
      num_numeral = "" # Reset
    end
  end

  num_array.reverse
end

def convert_base_20_to_10(digits_array)
  number = 0
  i = digits_array.size - 1
  while i >= 0
    number += digits_array[i].to_i * (BASE ** i)
    i -= 1
  end
  number
end

def convert_base_10_to_20(number)
  digits = Array.new
  i = 0

  if number == 0
    digits[0] = 0
    return digits
  end

  while number != 0
    digits[i] = number % BASE # remainder
    number = number / BASE
    i += 1
  end

  digits.reverse
end

@height.times do
  numeral = gets.chomp
  mayan_numerals.push(numeral)
end

# Store the mayan numerals in a hash
mayan_numeral = ''
column = 0
for i in 0..(BASE - 1) do
  mayan_numeral = ''
  column = i * @width

  mayan_numerals.each do |row|
    for j in column..(column + @width - 1) do
      mayan_numeral += row[j]
    end
    mayan_numeral += "\n"
  end

  @mayan_hash[mayan_numeral] = i
end

# Read the first and second number
num1_array = read_num
num1 = convert_base_20_to_10(num1_array)

num2_array = read_num
num2 = convert_base_20_to_10(num2_array)

operation = gets.chomp

# Calculate the result of the operation
result = case operation
           when '+' then
             num1 + num2
           when '-' then
             num1 - num2
           when '*' then
             num1 * num2
           when '/' then
             num1 / num2
           else
             0
         end

# Convert the result back to the original base
digits = convert_base_10_to_20(result)
digits.each do |digit|
  # Convert the digit to a mayan numeral
  mayan_numeral = @mayan_hash.key(digit)
  print mayan_numeral
end
