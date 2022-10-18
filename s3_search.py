#!/usr/bin/env python3.7
import boto3
resource=boto3.resource("s3")
for bucket in resource.buckets.all():
    print(bucket.name)
