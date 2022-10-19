#!usr/bin/env python3.7
#desribe available VPCs in you AWS account !
#!/usr/bin/env python3.7
import boto3
vpc_resource=boto3.client("ec2")
vpcs=vpc_resource.describe_vpcs()
#x=client.describe_vpcs()
no_of_vpcs=len(vpcs)
print(no_of_vpcs)

#for vpc in no_of_vpcs: # Need to fix this to show VPC names
 #  print(vpc)
