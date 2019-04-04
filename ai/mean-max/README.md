# Codingame Mean Max AI

## Wood 3 -> Bronze
**Reaper**
* My reaper moves to the closest wreck at 300 thrust.
* If there is no wreck, my reaper moves to the center of the map.

## Bronze -> Gold
**Reaper**
* My reaper moves to the wreck with the best score at 300 thrust.
* wreck score = water / distance to my reaper
* If there is no wreck, my reaper moves to my destroyer.

**Destroyer**
* My destroyer moves to the tanker with the best score at 300 thrust.
* tanker score = water / distance to my reaper
* If there is no tanker, my destroyer moves to to the center of the map.

**Doof**
* My doof uses his skill on the reaper of an enemy player if possible (prioritizing the enemy target).
* Otherwise, my doof moves to the reaper of the targeted enemy player.
* The enemy target is picked depending on the scoreboard.
* If I am in #1, I target #2.
* If I am in #2, I target #1.
* If I am in #3, I target #2 (to secure 2nd place).

All my looters apply the steering strategy.

## References
* [Codingame Referree](https://github.com/CodinGame/MeanMax)
* [Steering Strategy](https://tech.io/playgrounds/1003/flocking-autonomous-agents/steering-strategy)
* [robostac Postmortem](https://github.com/robostac/cg-meanmax-postmortem)
* [codingame-cpp-merge](https://github.com/wimgoeman/codingame-cpp-merge)

