#!/bin/bash

# Initialize variables
date=""
message=""

# Parse arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --date) 
            date="$2"
            shift 2
            ;;
        --message)
            message="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Check if date is provided
if [ -z "$date" ]; then
    echo "Error: --date is required"
    exit 1
fi

# Check if message is provided
if [ -z "$message" ]; then
    echo "Error: --message is required"
    exit 1
fi

# Add the date and message to the commitDates.txt file on a new line
echo "$date ==> $message" >> commitDates.txt

# Add the files to the commit
git add commitDates.txt

# Commit the files with the date and message
git commit --date="$date" -m "$message"

# Push the commit
git push origin main