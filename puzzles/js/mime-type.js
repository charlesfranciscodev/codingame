'use strict';

let map = {};

const pairCount = parseInt(readline()); // Number of elements which make up the association table.
const fileCount = parseInt(readline()); // Number of file names to be analyzed.
for (let i = 0; i < pairCount; ++i) {
  let inputs = readline().split(' ');
  let extension = inputs[0].toLowerCase(); // file extension
  let type = inputs[1]; // MIME type
  map[extension] = type;
}

// Debug
//for (let key in map)
//  printErr(key + '=' + map[key]);

// For each of the filenames, display on a line the corresponding MIME type.
// If there is no corresponding type, then display UNKNOWN.
for (let i = 0; i < fileCount; ++i) {
  let fileName = readline(); // One file name per line.
  let dotIndex = fileName.lastIndexOf('.');
  if ((dotIndex === -1) || (dotIndex === (fileName.length - 1))) {
    print('UNKNOWN');
  } else {
    let fileExt = fileName.substring(dotIndex + 1, fileName.length).toLowerCase();
    let mimeType = map[fileExt];
    if (mimeType === undefined)
      print('UNKNOWN');
    else
      print(mimeType);
  }
}
