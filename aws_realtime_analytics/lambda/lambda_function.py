# Lambda function to process records from a Kinesis stream
# Triggered automatically when records are available in the stream

def lambda_handler(event, context):
    # Loop through each record in the event
    for record in event['Records']:
        # Extract base64 encoded payload from Kinesis
        payload = record['kinesis']['data']
        
        # Log the payload (can be viewed in CloudWatch Logs)
        print("Received data:", payload)

    # Return a success response
    return {
        'statusCode': 200,
        'body': 'Processed records successfully'
    }
