

# Temperatures

The `Temperatures.swift` script is a solution to the "Temperatures" puzzle on the CodinGame platform. The goal of the puzzle is to find the temperature closest to zero among a list of temperatures. If there are two temperatures equally close to zero, the positive temperature should be considered closest to zero.

## Usage

The script can be run on the command line by passing in a list of temperatures separated by spaces:

```
$ swift temperatures.swift "1 -2 3 4 -5"
```

The script will then output the temperature closest to zero. If there are no temperatures provided, or if they are not valid integers, the script will output 0.

## Implementation

The script reads in the list of temperatures from the command line arguments and splits them into an array of integers. It then loops through the array, keeping track of the temperature closest to zero seen so far. If a temperature is found that is closer to zero than the current closest temperature, it becomes the new closest temperature. If the temperature is equally close to zero as the current closest temperature, and it is positive, it becomes the new closest temperature.

After looping through all the temperatures, the script outputs the closest temperature found.

## Example

```
$ swift temperatures.swift "-10 20 -30 40 50"
-10
```

In this example, the temperatures -10, 20, -30, 40, and 50 are passed in as command line arguments. The script loops through the temperatures and finds that -10 is the closest temperature to zero, so it outputs -10.