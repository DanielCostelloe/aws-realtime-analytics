# Script to generate and send sample events to an AWS Kinesis Data Stream

import json
import boto3
import base64
from datetime import datetime
import random
import time

# Initialize the Kinesis client (ensure AWS credentials are configured)
kinesis = boto3.client('kinesis', region_name='us-east-1')

# Function to generate a fake event record
def generate_event():
    return {
        "event_id": random.randint(1000, 9999),
        "event_type": random.choice(["click", "view", "purchase"]),
        "event_time": datetime.utcnow().isoformat(),
        "user_id": random.randint(1, 100)
    }

# Generate and send 10 events to the Kinesis stream
for _ in range(10):
    event = generate_event()
    
    # Encode the event as base64 (Kinesis expects binary data)
    encoded = base64.b64encode(json.dumps(event).encode('utf-8'))
    
    # Send the encoded event to the Kinesis stream
    kinesis.put_record(
        StreamName='realtime-data-stream',
        Data=encoded,
        PartitionKey='partitionKey'
    )
    
    # Print confirmation
    print("Sent event:", event)
    
    # Optional: wait 1 second between events
    time.sleep(1)
