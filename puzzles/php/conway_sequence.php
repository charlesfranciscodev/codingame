<?php
fscanf(STDIN, "%d", $original);
fscanf(STDIN, "%d", $lineNumber);

$sequence = [$original];

for ($line = 1; $line < $lineNumber; $line++) {
  // reset
  $tempSequence = [];
  $count = 0;

  error_log(var_export(implode(" ", $sequence), true));
  $previous = $sequence[0];
  foreach ($sequence as $number) {
    error_log(var_export($number, true));
    if ($number == $previous) {
      error_log(var_export($count, true));
      $count = $count + 1;
      error_log(var_export("same", true));
      error_log(var_export($count, true));
    } else {
      error_log(var_export("different", true));
      $tempSequence[] = $count;
      $tempSequence[] = $previous;
      $previous = $number;
      $count = 1;
    }
  }

  $tempSequence[] = $count;
  $tempSequence[] = $previous;
  $sequence = $tempSequence; // update
}

echo(implode(" ", $sequence));

// print(" ".join(map(str, sequence)))


// Write an action using echo(). DON'T FORGET THE TRAILING \n
// To debug (equivalent to var_dump): error_log(var_export($var, true));
?>
