import sys
import argparse
import boto3

parser = argparse.ArgumentParser()
parser.add_argument("value", help="enter a search term. See AWS documentation for wildcard syntax")
parser.add_argument("--field", "-f", default="description", help="enter the ami field you wish to search in. Default: description. Good alternative: name")
parser.add_argument("--region", "-r", default="*", help="enter the region to search for amis in. default: all")

args = parser.parse_args()

if args.region == "*":
    ec2 = boto3.client('ec2')
    regions = ec2.describe_regions()
    for region in regions['Regions']:
        regec2 = boto3.client('ec2',region_name=region['RegionName'])
        images = regec2.describe_images(Filters=[{'Name': args.field,'Values': [args.value,]}])
        print('\n\n'+region['RegionName'])
        for image in images['Images']:
            print('Name: '+image['Name'])
            print('Description: '+image['Description'])
            print('id: '+image['ImageId'])
else:
    regec2 = boto3.client('ec2',region_name=args.region)
    images = regec2.describe_images(Filters=[{'Name': args.field,'Values': [args.value,]}])
    for image in images['Images']:
        print('Name: '+image['Name'])
        print('Description: '+image['Description'])
        print('id: '+image['ImageId'])
