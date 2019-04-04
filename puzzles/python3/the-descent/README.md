# The Descent

The goal here is to prevent our ship from crashing into mountains.
In order to suceed, our ship must shoot the tallest mountain on each turn.
Therefore, we use the variable `max_mountain_height` to track the maximum height and also `index_mountain_to_fire` for the index to shoot.
On every turn, all mountain heights are read from the standard input.
We update our variables when a new maximum is found.
Finally, to write an action, we call the print function with `index_mountain_to_fire` as a parameter.
