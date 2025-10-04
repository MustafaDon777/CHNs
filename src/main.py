# main.py
import json
import datetime
import os
# import requests # Included in requirements.txt as an example of an external library

# Get the current time in UTC
current_time_utc = datetime.datetime.utcnow().isoformat()

# The data to write
data = {
    "message": "Hello World from a scheduled GitHub Action!",
    "run_time_utc": current_time_utc
}

# Define the file path (relative to the repository root)
output_file = 'output.json'

# Write the data to the JSON file
with open(output_file, 'w') as f:
    json.dump(data, f, indent=4)

print(f"Successfully wrote data to {output_file} at {current_time_utc}")