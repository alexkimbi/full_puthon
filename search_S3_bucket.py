#!/usr/bin/env python3.7
import boto3
s3 = boto3.client('s3')
response = s3.list_buckets()
buckets = response["buckets"]

for bucket in resource.buckets.all():
    print(bucket)

