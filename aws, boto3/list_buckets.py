import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def list_s3_buckets():
    try:
        # Create a session using the default profile (or specify your profile name)
        session = boto3.Session(profile_name='default')
        s3 = session.client('s3')
        
        # List S3 buckets
        response = s3.list_buckets()
        print("S3 Buckets:")
        for bucket in response['Buckets']:
            print(f" - {bucket['Name']}")
    
    except NoCredentialsError:
        print("Error: No credentials found. Please configure your AWS credentials.")
    except PartialCredentialsError:
        print("Error: Partial credentials found. Please ensure both access key and secret key are provided.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    list_s3_buckets()
