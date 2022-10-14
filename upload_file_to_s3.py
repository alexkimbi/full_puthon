#!/usr/bin/env python3.7
import boto3
s3_resource=boto3.client("s3")
s3_resource.upload_file(
    Filename="Configure_RDP_on_linux.txt", # name of the original file to be uploaded
    Bucket="boto3alexluit223",      # Name of the bucket to upload te file to 
    Key="Config_RDP_on.txt")  # Name of file to be identified in s3 bucket

print(s3_resource)