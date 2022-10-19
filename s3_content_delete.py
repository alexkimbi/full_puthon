#!/usr/bin/env python3.7

import boto3

client = boto3.client('s3')
client.delete_object(Bucket='boto3alexluit1', Key='20161104_040709000_iOS.mp4')


