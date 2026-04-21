import boto3

# Option 1: Use AWS profile (recommended)
session = boto3.Session(profile_name='your-profile-name')
s3 = session.client('s3')

# Option 2: Use environment variables (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
# s3 = boto3.client('s3')

# Option 3: Use explicit credentials (not recommended - use AWS profiles or IAM roles instead)
# s3 = boto3.client('s3',
#                   aws_access_key_id='YOUR_ACCESS_KEY_ID',
#                   aws_secret_access_key='YOUR_SECRET_ACCESS_KEY')

# Bucket name
bucket_name = 'your-bucket-name'

print(f"Working with bucket: {bucket_name}")

# Get bucket policy
try:
    policy = s3.get_bucket_policy(Bucket=bucket_name)['Policy']
    print(f"Bucket policy: {policy}")
        
except Exception as e:
    print(f"Error retrieving bucket policy: {e}")

# Delete Bucket policy (uncomment to use)
# try:
#     s3.delete_bucket_policy(Bucket=bucket_name)
#     print("Bucket policy deleted successfully.")
    
# except Exception as e:
#     print(f"Error deleting bucket policy: {e}")
