import boto3
s3 = boto3.client('s3')
response = s3.list_buckets()
print('Printing Existing buckets...:')
for bucket in response['Buckets']:
    print(f'  {bucket["CreationDate"]}') # Take out the [] and the "CreationDate" and you will see the S3 uckets and all info related