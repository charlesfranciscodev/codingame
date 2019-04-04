<?php
fscanf(STDIN, "%d", $nbVoters);
fscanf(STDIN, "%d", $totalVotes);
$voterList = [];
for ($i = 0; $i < $nbVoters; $i++) {
  fscanf(STDIN, "%s %d", $personName, $nbVotes);
  $voterList[$personName] = $nbVotes;
}

// Filter the results
$results = [];
for ($i = 0; $i < $totalVotes; $i++) {
  fscanf(STDIN, "%s %s", $voterName, $voteValue);
  $result = [$voterName, $voteValue];
  if (array_key_exists($voterName, $voterList)) {
    // Check if the voter did not over vote
    $nbVotes = $voterList[$voterName];
    if ($nbVotes != 0) {
      if ($voteValue == "Yes" || $voteValue == "No") {
        $voterList[$voterName]--;
        array_push($results, $result);   
      }
    } else {
      // Invalidate all his votes
      unset($voterList[$voterName]);
      $results = array_filter($results, function($result, $key) use($voterName) {
        return $result[0] != $voterName;
      }, ARRAY_FILTER_USE_BOTH);

    }
  }
}

// Count the results
$yesCount = 0;
$noCount = 0;
foreach ($results as $result) {
  if ($result[1] == "Yes") {
    $yesCount++;
  } else {
    $noCount++;
  }
}

echo("$yesCount $noCount\n");
?>
