#!/usr/bin/env python3.7
# Importing boto3 library to make functionality available
import boto3
# Creating the connection with the resource of AWS EC2 service 
ec2 = boto3.resource('ec2')
# Adding the Tag Boto3 for AWS EC2 using the instance ID
response = ec2.create_tags(
    Resources=[
        'i-00ebfd23957a1c6a1',    # EC2 Instance ID  
    ],
    Tags=[
        {
            'Key': 'Name',
            'Value': 'Boto3_test' #
        },
    ]
)
