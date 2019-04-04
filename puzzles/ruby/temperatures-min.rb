n=gets.to_i
m=5526
i=gets.split.map(&:to_i)
for t in i
m=t if t.abs<m.abs||t.abs==m.abs&&t>m
end
puts n==0?0:m
