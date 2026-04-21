import boto3
S3_SERVICE = "s3"
SNS_SERVICE = "sns"


def get_s3_resource():
    """
    return initialized boto3 S3 Client
    """
    return boto3.resource(S3_SERVICE, verify=False)


def delete_folder_from_s3(bucket_name, folder_path, s3_resource=None):
    s3 = get_s3_resource() if not s3_resource else s3_resource
    bucket = s3.Bucket(bucket_name)

    for obj in bucket.objects.filter(Prefix=folder_path):
        obj_key = obj.key
        
        print(f"Deleting: {obj_key}")
        obj.delete()
        print(f"Deleted: {obj_key}")