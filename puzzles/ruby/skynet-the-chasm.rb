STDOUT.sync = true # DO NOT REMOVE

@road = gets.to_i # the length of the road before the gap.
@gap = gets.to_i # the length of the gap.
@platform = gets.to_i # the length of the landing platform.

jump = false; # true == the gap was jumped

# game loop
loop do
  speed = gets.to_i # the motorbike's speed.
  coord_x = gets.to_i # the position on the road of the motorbike.

  if (speed < (@gap + 1)) && !jump
    # Increase the speed in case it is not sufficient to jump the gap
    puts "SPEED"
  elsif (speed > (@gap + 1)) && !jump
    # Decrease the speed in case it is over the gap's length
    puts("SLOW")
  elsif (coord_x == (@road - 1)) && !jump
    # Jump the gap at the end of the road
    puts("JUMP")
    jump = true
  elsif coord_x >= (@road + @gap)
    # After the jump, slow down
    puts("SLOW")
  else
    puts("WAIT")
  end

  # Write an action using puts
  # To debug: STDERR.puts "Debug messages..."
end