<?php
$map = array();
fscanf(STDIN, "%d", $tableSize); // Number of elements which make up the association table.
fscanf(STDIN, "%d", $fileCount); // Number of file names to be analyzed.
for ($i = 0; $i < $tableSize; ++$i) {
  fscanf(STDIN, "%s %s", $extension, $type); // file extension and MIME type.
  $map[strtolower($extension)] = $type;
}

// For each of the filenames, display on a line the corresponding MIME type.
// If there is no corresponding type, then display UNKNOWN.
for ($i = 0; $i < $fileCount; ++$i) {
  $name = strtolower(stream_get_line(STDIN, 501, "\n")); // One file name per line.
  $dotIndex = strrpos($name, '.');
  if ($dotIndex === false || $dotIndex == (strlen($name) - 1)) {
    echo("UNKNOWN\n");
  } else {
    $extension = substr($name, $dotIndex + 1);
    echo array_key_exists($extension, $map) ? "$map[$extension]\n" : "UNKNOWN\n";
  }
}
?>
