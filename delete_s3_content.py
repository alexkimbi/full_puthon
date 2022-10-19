#!/usr/bin/env python3.7
import boto3
vpc_resource=boto3.client("ec2")
vpcs=vpc_resource.describe_vpcs()
print(vpcs)