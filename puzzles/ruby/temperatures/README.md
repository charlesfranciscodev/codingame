# Temperatures

## Description

"Temperatures" is a beginner-level coding challenge available on the CodinGame platform. In this challenge, the player is given a list of integers representing temperature readings in Celsius degrees for a city during a certain period of time.

The objective is to write a program that finds and outputs the closest temperature to zero. If there are two temperatures that are equally close to zero, the program should output the positive one.

The challenge consists of writing a program that takes as input the list of temperature readings and outputs the temperature closest to zero. If the list is empty, the program should output 0.

## Solution Overview

The solution to this challenge involves iterating over the list of temperatures and keeping track of the absolute difference between each temperature and zero. The closest temperature to zero is the one with the smallest absolute difference. If there are two temperatures with the same absolute difference, the solution should output the positive one.

## Example Input/Output

**Input**

```
5
1 -2 -8 4 5
```

**Output**

```
1
```

## Code Example

```ruby
# Initialize variables
closest_temp = nil
closest_diff = nil

# Read the number of temperatures to analyze
n = gets.to_i

# Read the temperatures as a string and split it into a list of integers
temperatures = gets.split(" ").map(&:to_i)

# Find the temperature closest to zero
temperatures.each do |temperature|
    # Calculate the absolute difference between the temperature and zero
    diff = (temperature - 0).abs
    # Check if the current temperature is closer to zero, handling the case where the closest difference is unknown
    if closest_temp.nil? || diff < closest_diff
        closest_temp = temperature
        closest_diff = diff
    # choose the positive one by comparing the temperature with zero
    elsif diff == closest_diff && temperature > 0
        closest_temp = temperature
    end
end

# Print the closest temperature
puts closest_temp || 0
```
