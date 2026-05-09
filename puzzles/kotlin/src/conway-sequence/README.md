# Conway Sequence

This is the Kotlin implementation for the "Conway Sequence" puzzle on CodinGame.

## Problem Description

Conway's Sequence is a sequence of numbers, starting with a 1, such that each subsequent number is a description of the previous number.

To generate a member of Conway's Sequence from the previous member, read off the digits of the previous member, counting the number of digits in groups of the same digit. For example, 1 is read off as "one 1" or 11, 11 is read off as "two 1s" or 21, 21 is read off as "one 2, then one 1" or 1211, and so on.

Your task is to implement a function that generates the nth member of Conway's Sequence.

## Solution

The solution to this problem is to generate each member of the sequence, starting from 1, until we reach the nth member. To generate each member, we need to read off the digits of the previous member, counting the number of digits in groups of the same digit.

We can do this using two nested loops. The outer loop generates each member of the sequence, while the inner loop reads off the digits of the previous member and counts the number of digits in groups of the same digit.
