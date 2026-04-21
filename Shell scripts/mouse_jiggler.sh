#!/bin/bash

# Define the duration between mouse movements (in seconds)
interval=60  # 5 minutes

while true; do
    # Move the mouse cursor slightly to prevent sleep
    osascript -e 'tell application "System Events" to do shell script "echo move 1"'

    # Sleep for the defined interval
    sleep $interval
done
