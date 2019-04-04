/**
 * CodinGame planet is being attacked by slimy insectoid aliens.
 * <---
 * Hint:To protect the planet, you can implement the pseudo-code provided in the statement, below the player.
 **/

// game loop
while (true) {
  let enemy1 = readline(); // name of enemy 1
  let dist1 = parseInt(readline()); // distance to enemy 1
  let enemy2 = readline(); // name of enemy 2
  let dist2 = parseInt(readline()); // distance to enemy 2
  
  if (dist1 < dist2) {
    console.log(enemy1);
  } else {
    console.log(enemy2);
  }
}
