#!/usr/bin/env pyhon3.7
services_list = []
services_list.append('ECR')
services_list.append('LAMBDA')
services_list.append('EC2')
services_list.append('IAM')
print("Total number of services:",services_list)
print("The lengh of services_list is:", len(services_list))
del services_list[1:3]
print("The new of lengh of services after two deleted:", len(services_list))
print("Services after two deleted:", services_list)