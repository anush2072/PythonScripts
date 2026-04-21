# Test connectivity to an endpoint - in AWS Lambda
import requests

def lambda_handler(event, context):
    # Replace with your target endpoint URL
    endpoint_url = 'https://your-endpoint.example.com'
    
    try:
        response = requests.get(endpoint_url)
        response.raise_for_status()

        return {
            "statusCode": 200,
            "body": response.text
        }

    except requests.RequestException as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }
