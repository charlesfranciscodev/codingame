# Horse Racing Duals

You have a list of N horses, each with a strength value, represented by an integer. You need to find the minimum difference in strength between two horses out of all possible pairs of horses. In other words, you need to find the two horses with the closest strength values.

For example, given the following list of horses with their corresponding strength values:

```
5 8 9 14 21
```

The minimum difference in strength between two horses is 1, which is the difference between 8 and 9.

The input for the problem consists of two lines. The first line contains an integer N, the number of horses. The second line contains N space-separated integers, representing the strength values of the N horses.

The output should be a single integer, the minimum difference in strength between two horses.

The solution to this problem involves sorting the list of horses in ascending order, and then computing the difference between adjacent horses in the sorted list. The minimum difference is the smallest of these computed differences.
