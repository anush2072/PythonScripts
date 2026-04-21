#!/bin/zsh

# Set the directory where your files are located
directory="<FOLDER_PATH_HERE>"

# Change to the directory
cd "$directory" || exit 1

# Iterate through each file in the directory
for file in *; do
    # Check if the file is a regular file
    if [[ -f "$file" ]]; then
        # Extract the base name (without extension)
        base_name=${file%.*}
        
        # Extract the extension
        extension=${file##*.}
        
        # Check if a file with the same base name and (1) exists
        if [[ -f "${base_name}_3.${extension}" ]]; then
            # If the duplicate file exists, delete it
            rm -f "${base_name}_3.${extension}"
            # mv file file2 – to rename a file use mv command followed by original file name, space and then new file name
            # mv "${base_name}~2.${extension}" "${base_name}.${extension}"
            echo "Deleted ${base_name}_3.${extension}"
        fi
    fi
done

echo "Duplicate files have been deleted."
