// @ts-nocheck

const N: number = parseInt(readline()); // Number of elements which make up the association table.
const Q: number = parseInt(readline()); // Number Q of file names to be analyzed.

const mimeTable: { [key: string]: string } = {};

// Reading the MIME type associations.
for (let i = 0; i < N; i++) {
    const inputs: string[] = readline().split(' ');
    const EXT: string = inputs[0].toLowerCase(); // file extension (converted to lowercase for case-insensitivity)
    const MT: string = inputs[1]; // MIME type
    mimeTable[EXT] = MT; // Store the MIME type with the extension as the key
}

// Processing each file name.
for (let i = 0; i < Q; i++) {
    const FNAME: string = readline();
    
    // Find the position of the last '.' in the file name.
    const lastDotIndex = FNAME.lastIndexOf('.');

    // If there's a '.' and it isn't the last character, extract the extension.
    if (lastDotIndex !== -1 && lastDotIndex < FNAME.length - 1) {
        const fileExt = FNAME.slice(lastDotIndex + 1).toLowerCase(); // Get the file extension and convert to lowercase
        
        // Check if the extension exists in the mimeTable.
        if (mimeTable.hasOwnProperty(fileExt)) {
            console.log(mimeTable[fileExt]); // Output the MIME type
        } else {
            console.log('UNKNOWN'); // Output UNKNOWN if extension not found
        }
    } else {
        console.log('UNKNOWN'); // Output UNKNOWN if no extension or '.' at the end
    }
}
