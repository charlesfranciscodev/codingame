STDOUT.sync = true # DO NOT REMOVE
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

@surface_n = gets.to_i # the number of points used to draw the surface of Mars.
@surface_n.times do
  # land_x: X coordinate of a surface point. (0 to 6999)
  # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
  land_x, land_y = gets.split(" ").collect {|x| x.to_i}
end

# game loop
loop do
  # h_speed: the horizontal speed (in m/s), can be negative.
  # v_speed: the vertical speed (in m/s), can be negative.
  # fuel: the quantity of remaining fuel in liters.
  # rotate: the rotation angle in degrees (-90 to 90).
  # power: the thrust power (0 to 4).
  x, y, h_speed, v_speed, fuel, rotate, power = gets.split(" ").collect {|x| x.to_i}

  # Write an action using puts
  # To debug: STDERR.puts "Debug messages..."

  if v_speed <= -40
    puts "0 4"
  else
    puts "0 0"
  end

  # 2 integers: rotate power. rotate is the desired rotation angle (should be 0 for level 1), power is the desired thrust power (0 to 4).
  # puts "0 3"
end