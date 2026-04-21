#!/bin/bash

# Set your MySQL credentials
MYSQL_USER="your_mysql_user"
MYSQL_PASSWORD="your_mysql_password"

# Set the MySQL host and port
MYSQL_HOST="your-mysql-host.example.com"  # Replace with the actual host
MYSQL_PORT="3306"  # Replace with the actual port, e.g., 3306

# Set the user whose queries you want to terminate
TARGET_USER="target_username"

# Get a list of connection IDs for the specified user
CONNECTION_IDS=$(mysql -h $MYSQL_HOST -P $MYSQL_PORT -u $MYSQL_USER -p$MYSQL_PASSWORD -e "SELECT ID FROM information_schema.processlist WHERE USER = '$TARGET_USER';" | tail -n +2)

# Loop through each connection ID and kill the associated query
for CONNECTION_ID in $CONNECTION_IDS; do
    echo $CONNECTION_ID
    mysql -h $MYSQL_HOST -P $MYSQL_PORT -u $MYSQL_USER -p$MYSQL_PASSWORD -e "KILL $CONNECTION_ID"
    echo "done!"
done
