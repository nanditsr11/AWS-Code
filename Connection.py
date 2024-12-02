import boto3
from botocore.exceptions import NoCredentialsError

# Set up AWS credentials (access and secret keys) - Alternatively, use AWS CLI config for automatic authentication
aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'
region_name = 'us-west-2'  # Change to your region

# Initialize an S3 client
s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id,
                         aws_secret_access_key=aws_secret_access_key,
                         region_name=region_name)

# Define the file and bucket details
local_file_path = 'path/to/your/local/file.txt'  # Change to your file path
bucket_name = 'your-s3-bucket-name'
s3_file_name = 'uploaded_file.txt'  # Change this to the desired S3 file name

def upload_to_aws(local_file, bucket, s3_file):
    try:
        print(f"Uploading {local_file} to {bucket}/{s3_file}...")
        s3_client.upload_file(local_file, bucket, s3_file)
        print(f"Upload Successful to {bucket}/{s3_file}")
    except FileNotFoundError:
        print(f"The file {local_file} was not found")
    except NoCredentialsError:
        print("Credentials not available")

# Call the upload function
upload_to_aws(local_file_path, bucket_name, s3_file_name)
