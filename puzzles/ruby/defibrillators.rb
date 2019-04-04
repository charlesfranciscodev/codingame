# Convert degrees to radians
def to_radians(degrees)
  degrees.to_f * Math::PI / 180
end

def format_degrees(distance)
  to_radians(distance.chomp.gsub(',', '.'))
end

EARTH_RADIUS = 6371
NAME = 1
LONGITUDE = 4
LATITUDE = 5

min = Float::MAX
name = ''

longitude = format_degrees(gets)
latitude = format_degrees(gets)
defib_count = gets.to_i

# Determine the name of the defibrillator
# located the closest to the user’s position.
defib_count.times do
  defib = gets.chomp
  defibArray = defib.split(';')
  defibLon = format_degrees(defibArray[LONGITUDE])
  defibLat = format_degrees(defibArray[LATITUDE])
  x = (defibLon - longitude) * (Math.cos((latitude + defibLat) / 2))
  y = defibLat - latitude
  distance = Math.hypot(x, y) * EARTH_RADIUS
  if distance < min
    min = distance
    name = defibArray[NAME]
  end
end

puts name
