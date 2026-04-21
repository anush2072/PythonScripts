#!/bin/bash

export AWS_PROFILE='your-aws-profile'
bucket_name="your-bucket-name"
root_folder="your-root-folder"
log_file="./s3_file_counts.log"

echo "" >> "$log_file"
echo Current Date and Time : `date +"%Y-%m-%d %T"` >> "$log_file"
# echo "s3://$bucket_name/$root_folder"

# List all the folders within the bucket
folders=($(aws s3 ls "s3://$bucket_name/$root_folder/" | awk '{print $2}'))

# Iterate through the folders and count the number of files in each folder
for folder in "${folders[@]}"; do
    file_count=$(aws s3 ls "s3://$bucket_name/$root_folder/$folder" --recursive | wc -l)
    echo "Folder: $folder, File Count: $file_count" >> "$log_file"
done

unset AWS_PROFILE

echo "" >> "$log_file"
echo "" >> "$log_file"