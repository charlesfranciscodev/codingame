def mime_type_puzzle():
    # Number of elements which make up the association table.
    N = int(input())

    # Number of file names to be analyzed.
    Q = int(input())

    mime_table = {}

    # Reading the MIME type associations.
    for _ in range(N):
        ext, mime_type = input().split()
        mime_table[ext.lower()] = mime_type  # Store extensions as lowercase for case-insensitivity.

    # Processing each file name.
    for _ in range(Q):
        fname = input()
        
        # Find the position of the last '.' in the file name.
        last_dot_index = fname.rfind('.')
        
        # If there's a '.' and it isn't the last character, extract the extension.
        if last_dot_index != -1 and last_dot_index < len(fname) - 1:
            file_ext = fname[last_dot_index + 1:].lower()  # Get the file extension and convert to lowercase.
            
            # Check if the extension exists in the mime_table.
            if file_ext in mime_table:
                print(mime_table[file_ext])  # Output the MIME type.
            else:
                print('UNKNOWN')  # Output UNKNOWN if extension not found.
        else:
            print('UNKNOWN')  # Output UNKNOWN if no extension or '.' at the end.


if __name__ == "__main__":
    mime_type_puzzle()
