# For each of the Q filenames, display on a line the corresponding MIME type.
# If there is no corresponding type, then display UNKNOWN.

hash = Hash.new
fileExtension = ""
mimeType = ""
dotIndex = 0

@pairCount = gets.to_i # Number of elements which make up the association table.
@filesCount = gets.to_i # Number Q of file names to be analyzed.

@pairCount.times do
  # ext: file extension
  # mt: MIME type.
  ext, mt = gets.split(" ")
  ext = ext.downcase
  hash.store(ext, mt)
end

#Test
# hash.each do |ext, mt|
#   STDERR.puts "#{ext} #{mt}"
# end

@filesCount.times do
  fileName = gets.chomp # One file name per line.
  #STDERR.puts(fileName)
  dotIndex = fileName.rindex('.')
  #STDERR.puts(dotIndex)
  if dotIndex == nil
    puts "UNKNOWN"
  elsif (dotIndex >= 0) && (dotIndex < (fileName.length - 1))
    fileExtension = fileName[dotIndex + 1 .. -1].downcase
    #STDERR.puts(fileExtension)
    mimeType = hash.fetch(fileExtension, 'UNKNOWN')
    puts(mimeType)
  else
    puts "UNKNOWN"
  end
end