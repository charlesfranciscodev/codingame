# Acid Oxide Name Generator

This Python script generates the name of an acid oxide based on the input parameters provided by the user.

## Problem Statement

Given a nonmetal element represented by its atomic number, symbol, and the number of oxygen atoms bonded to it, the task is to generate the name of the corresponding acid oxide according to the IUPAC nomenclature rules.

## Solution Overview

The script defines a function `acid_oxide_name` which takes three parameters:
- `nonmetalNum`: An integer representing the atomic number of the nonmetal element.
- `nonmetal`: A string representing the symbol of the nonmetal element.
- `oxideNum`: An integer representing the number of oxygen atoms bonded to the nonmetal element.

It then generates the name of the acid oxide based on the input parameters using the following rules:
- It uses predefined lists `nonmetal_prefixes` and `oxide_prefixes` to map the numerical prefixes to their corresponding string prefixes.
- If the numerical prefix is 1, it uses an empty string for the nonmetal prefix and "mon" for the oxide prefix.
- Otherwise, it uses the appropriate prefix from the lists.
- Finally, it concatenates the nonmetal prefix, nonmetal symbol, space, and oxide prefix with "oxide" to generate the name of the acid oxide.

In the main block:
- It takes input from the user for `nonmetalNum`, `nonmetal`, and `oxideNum`.
- Calls the `acid_oxide_name` function with the provided inputs.
- Prints the generated acid oxide name.

## Note

- This script assumes valid input values are provided.
- The generated acid oxide name follows IUPAC nomenclature rules for acid oxides.
