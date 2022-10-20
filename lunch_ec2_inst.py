#!/usr/bin/env python3.7
# Importing boto3 library to make functionality available
import boto3
# Creating the connection with the resource of AWS EC2 service
ec2 = boto3.resource('ec2')
# creating a new EC2 instance
instances = ec2.create_instances(
      ImageId='ami-013f17f36f8b1fefb',
      MinCount=1,
      MaxCount=1,
      InstanceType='t2.micro',
  )
print("EC2 Launched succesfully")