number = gets.to_i
sum = 1

for i in 2..number
  max = Math.sqrt(i).to_i # Update max
  sum += 1 + i # 1 and i are always divisors
  for j in 2..max
    if (i % j) == 0
      sum += j
      quotient = i / j
      if quotient != j
        sum += quotient
      end
    end
  end
end

puts sum