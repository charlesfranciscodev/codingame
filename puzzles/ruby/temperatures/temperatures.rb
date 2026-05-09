n = gets.to_i # the number of temperatures to analyze
inputs = gets.split(" ").map(&:to_i)

closest_temperature = nil
closest_difference = nil

inputs.each do |t|
  difference = (t - 0).abs
  if closest_difference.nil? || difference < closest_difference || (difference == closest_difference && t > 0)
    closest_temperature = t
    closest_difference = difference
  end
end

puts closest_temperature || 0
