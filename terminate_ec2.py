#!/usr/bin/env python3

import boto3

AWS_REGION = "us-east-1" #Edit the AWS_REGION where the instance is located
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
INSTANCE_ID = 'i-0ad36097c1a3699ec'   # Edit the Instance ID

instance = EC2_RESOURCE.Instance(INSTANCE_ID)

instance.terminate()

print(f'Terminating EC2 instance: {instance.id}')
    
instance.wait_until_terminated()

print(f'EC2 instance "{instance.id}" has been terminated')
