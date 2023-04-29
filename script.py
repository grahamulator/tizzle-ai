#!/bin/bash

# Read the CSV file
while IFS=',' read -r host name gpu
do
  # Print to the console
  echo "Checking: $name ($host) - Running: $gpu";
  
  # Do something with the variables
  sshpass -f secrets ssh admin@$host 'ls ~/Desktop/keyhunt |grep KEY';

done < hosts.csv