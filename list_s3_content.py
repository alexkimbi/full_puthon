#!/usr/bin/env python3.7
import boto3
s3_resource=boto3.client("s3")
objects=s3_resource.list_objects(Bucket="boto3alexluit1")["Contents"]
len(objects)
if len(objects)>0:
    print("Obects exist")
    print(objects)
#for object in objects:
 #   print(object["key"])
    
#print(object)